from rest_framework import serializers
from .models import Employee, Object, Position, Mode, Call_Status, Call_Type, Type_ChP, Status_ChP, Period, Plan,Plan_raw,Tick_ChP, Close_ChP, Call

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'
    
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
    
class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = '__all__'
    
class Call_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call_Status
        fields = '__all__'
    
class Call_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call_Type
        fields = '__all__'
    
class Type_ChPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_ChP
        fields = '__all__'

class Status_ChPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status_ChP
        fields = '__all__'
    
class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'
    
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
    
class Plan_rawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan_raw
        fields = '__all__'

class Tick_ChPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tick_ChP
        fields = '__all__'
    
    
    
class Close_ChPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Close_ChP
        fields = '__all__'
    
class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'