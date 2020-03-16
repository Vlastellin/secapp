from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser 
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.forms.models import model_to_dict
from rest_framework import status
from .models import Employee, Object, Position, Mode, Call_Status, Call_Type, Type_ChP, Status_ChP, Period, Plan,Plan_raw,Tick_ChP, Close_ChP, Call
from .serializers import *
# Create your views here.


class Call_v(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer

class Close_ChP_v(viewsets.ModelViewSet):
    queryset = Close_ChP.objects.all()
    serializer_class = Close_ChPSerializer

class Tick_ChP_v(viewsets.ModelViewSet):
    queryset = Tick_ChP.objects.all()
    serializer_class = Tick_ChPSerializer

class Plan_raw_v(viewsets.ModelViewSet):
    queryset = Plan_raw.objects.all()
    serializer_class = Plan_rawSerializer

class Plan_v(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class Period_v(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class Status_ChP_v(viewsets.ModelViewSet):
    queryset = Status_ChP.objects.all()
    serializer_class = Status_ChPSerializer
    
class Type_ChP_v(viewsets.ModelViewSet):
    queryset = Type_ChP.objects.all()
    serializer_class = Type_ChPSerializer


class Call_Type_v(viewsets.ModelViewSet):
    queryset = Call_Type.objects.all()
    serializer_class = Call_TypeSerializer


class Call_Status_v(viewsets.ModelViewSet):
    queryset = Call_Status.objects.all()
    serializer_class = Call_StatusSerializer

class Mode_v(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer



class Position_v(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


#@csrf_exempt    
class Object_v(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    
class Employee_v(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
        
class Verify(viewsets.ModelViewSet): 
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request, format=None):
        return Response("test")
    
    @action(detail=False, methods=['POST'], name='Post Highlight')
    def get(self, request, format=None):
        return Response("test")
    
    def POST(self,request):
        data = JSONParser().parse(request)
        login =data['employee_login']
        password= data['employee_password']
        employes = Employee.objects.all()
        for obj in employes:
            if (obj.employee_login==login)and(obj.employee_password==password):
                return JsonResponse({"answer": "True", "id": obj.employee_id, "fio": obj.employee_fio}, safe=False)
        return JsonResponse({"answer": "False"}, safe=False)
    
class Verify2(APIView): 
 
    def post(self,request):
        data = JSONParser().parse(request)
        login =data['employee_login']
        password= data['employee_password']
        employes = Employee.objects.all()
        for obj in employes:
            if (obj.employee_login==login)and(obj.employee_password==password):
                return JsonResponse({"answer": "True", "id": obj.employee_id, "fio": obj.employee_fio}, safe=False)
        return JsonResponse({"answer": "False"}, safe=False)
    

def day_to_word(day):
        print("!!!!!!! ", day)
        if day==0:
            return "пн"
        elif day==1:
            return "вт"
        elif day==2:
            return "ср"
        elif day==3:
            return "чт"
        elif day==4:
            return "пт"
        elif day==5:
            return "сб"
        elif day==6:
            return "вс"
        else:
            return "error"
    
def create_position_list():
        positions = Position.objects.all()
        result=[]
        for position in positions:
            result.append({"position_id":position.position_id, "position":position.position_phone_number, "object": position.position_object.object_name,"object_id":position.position_object.object_id})
        print(result)
        return result

def find_last_plan(position_id, day_word):
    plan_list =list( filter(lambda x : x.plan_day ==day_word and x.plan_position.position_id==position_id , Plan.objects.all()))
    print("-----")
    print(plan_list)
    print(day_word)
    print(position_id)
    max_plan = plan_list[0]
    for plan in plan_list:
        if plan.plan_date>max_plan.plan_date:
            max_plan=plan
    return max_plan

def fill_plan_raw(list_plan_raw, plan_id):
    plan_raws = list(filter(lambda x : x.plan_raw_plan.plan_id==plan_id ,Plan_raw.objects.all()))
    print("plan_id ", type(plan_raws))
    for plan_raw in plan_raws:
        hour = plan_raw.plan_raw_period.period_value.split(":")[0]
        print("plan_raw", hour)
        if hour in list_plan_raw.keys():
            list_plan_raw[hour]["status"]=0
    
    
def mark_call(list_plan_raw, date, position):
    d_b = datetime.datetime(date.year, date.month, date.day, 7, 30, 0)
    date_next =(date +datetime.timedelta(days=1))
    d_f= datetime.datetime(date_next.year, date_next.month, date_next.day, 4, 30, 0)
    marks = list(filter(lambda x : datetime.datetime(x.call_date.year, x.call_date.month, x.call_date.day, x.call_time.hour, x.call_time.minute, x.call_time.second)>=d_b and datetime.datetime(x.call_date.year, x.call_date.month, x.call_date.day, x.call_time.hour, x.call_time.minute, x.call_time.second)<=d_f  ,Call.objects.all()))
    for mark in marks:
        hour = mark.call_time.hour
        if mark.call_time.minute> 44:
            hour = (hour+1)%24
        if str(hour) in list_plan_raw.keys() and list_plan_raw[str(hour)]["status"]==0:
            list_plan_raw[str(hour)]["status"]=2
            list_plan_raw[str(hour)]["call_id"]=mark.call_id
            list_plan_raw[str(hour)]["call_datetime"]=datetime.datetime(mark.call_date.year, mark.call_date.month, mark.call_date.day, mark.call_time.hour, mark.call_time.minute, mark.call_time.second)
            list_plan_raw[str(hour)]["call_link"]=mark.call_path
            list_plan_raw[str(hour)]["employee"]=mark.call_employee.employee_fio
            
            
            
    
    
def create_raw(position, date):#
        day =date.weekday()
        if date.hour<8:
            day= (day-1+7)%6
        day_word= day_to_word(day)
        plan = find_last_plan(position["position_id"], day_word)
        #найти строки плана и отметки
        list_plan_raw={"8":{"status":1}, "12":{"status":1}, "16":{"status":1}, "17":{"status":1}, "18":{"status":1}, "20":{"status":1}, "0":{"status":1}, "4":{"status":1}, "mode":plan.plan_mode.mode_value}
        fill_plan_raw(list_plan_raw, plan.plan_id)
        mark_call(list_plan_raw, date, position)
        return list_plan_raw
        
class Today(APIView):     
    
 
    def post(self,request):
        import datetime
        #узнать текущую дату
        date = datetime.datetime.now()
        position_list =create_position_list()
        #список всех обьектов и их постов
        data =[]
        for position in position_list:
            row = create_raw(position,date)
            row["position_number"]=position["position"]
            row["position_id"]=position["position_id"]
            row["object_name"]=position["object"]
            row["object_id"]=position["object_id"]
            data.append(row)
        
        return JsonResponse(data, safe=False)

class Enter_to_job(APIView): 
    
 
    def post(self,request, video_file):
        
        data = JSONParser().parse(request)
        date = datetime.datetime.now()
        data_call= {}
        
        data_call["call_date"]=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
        data_call["call_time"]=str(date.hour)+":"+str(date.minute)+":"+str(date.second)
        data_call["call_position"]=data["call_position"]
        data_call["call_employee"]=data["call_employee"]
        data_call["call_type"]=1
        data_call["call_status"]=1
        filename="./video_files/"+data["filename"]#+str(data_call["call_position"])+str(date)+".mp4"
        data_call["call_path"]=filename
        save_file=open(filename, 'wb')
        save_file.write(video_file)
        save_file.close()
        serializer = CallSerializer(data=data_call)
        if serializer.is_valid():
                serializer.save() 
                return JsonResponse({"answer": "Created"}, safe=False) 
        return JsonResponse({"answer": "Error"}, safe=False)
        
        
    
class This_day(APIView): 
    def post(self,request):
        import datetime
        #узнать текущую дату
        #список всех обьектов и их постов
        #пойти по списку формируя таблицу
        #
        #
        data = [json.dumps({"object":"RT", "position":"Kazan", "employee":"Manul", "time_8":2, "time_12":2, "time_16":1, "time_17":1, "time_18":1, "time_20":1, "time_24":0, "time_4":0, "mode":"night"}), json.dumps({"object":"RT", "position":"Kazan", "employee":"Zaharov", "time_8":2, "time_12":1, "time_16":0, "time_17":1, "time_18":1, "time_20":1, "time_24":0, "time_4":0, "mode":"day"})]
        return JsonResponse({"data":3}, safe=False)
    
class TickView2(APIView):
    def post(self,request):
        data = JSONParser().parse(request)
        if data['table_name']=='Employee':
            if data['flag']=='verify':
                login =data['employee_login']
                password= data['employee_password']
                employes = Employee.objects.all()
                for obj in employes:
                    if (obj.employee_login==login)and(obj.employee_password==password):
                        return JsonResponse({"answer": "True"}, safe=False)
                return JsonResponse({"answer": "False"}, safe=False)
            elif data['flag']=='registration':
                del data['flag']
                serializer = EmployeeSerializer(data=data)
                if serializer.is_valid():
                    serializer.save() 
                    return JsonResponse({"answer": "Created"}, safe=False) 
                return JsonResponse({"answer": "Error"}, safe=False) 
            else:
                return JsonResponse({"answer": "flag do not recognize"}, safe=False)
        else:
            return JsonResponse({"answer": "can't find table with this name"}, safe=False)
        
    def get(self,request):
        data = JSONParser().parse(request)
        if data['table_name']=='Employee':
            employes = Employee.objects.all()
            serializer = EmployeeSerializer(employes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"answer": "can't find table with this name"}, safe=False)
        