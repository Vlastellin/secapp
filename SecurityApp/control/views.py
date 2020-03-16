from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse


def login_index(request):
    if request.method == "POST":
        return redirect("/table")
    else:
        return render(request, 'login.html')


def redirect_login(request):
    #data_login = requests.get('http://185.27.194.131/security/app/employee/').text
    #data_login = json.loads(data_login)
    #login = request.GET.get('login')
    #password = request.GET.get('password')
    #for item in data_login:
    #    if login == item["employee_login"] and password == item["employee_password"]:
    #        return redirect('table')
    #    else:
    #        return HttpResponse("Неверный логин или пароль.")
	return HttpResponse("Неверный логин или пароль.")
	

def index(request):
    return render(request, 'index.html')
