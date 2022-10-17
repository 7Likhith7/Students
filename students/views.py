from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from django.template import loader
# from django.views.decorators.csrf import csrf_exempt
from .models import Students
from django.urls import reverse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    students = Students.objects.all().values()
    params = {
        "students" : students
    }
    return HttpResponse(template.render(params, request))

# @csrf_exempt
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST['name']
    address = request.POST['address']
    student = Students(name = name, address = address)
    student.save()
    return HttpResponseRedirect(reverse("index"))

def returning(request):
    return HttpResponseRedirect(reverse("index"))

def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return HttpResponseRedirect(reverse("index"))

def update(request, id):
    template = loader.get_template("update.html")
    student = Students.objects.get(id=id)
    print(student)
    params = {
        "student" : student
    }
    return HttpResponse(template.render(params, request))

def updaterecord(request, id):
    new_name = request.POST['name']
    new_address = request.POST['address']
    student = Students.objects.get(id=id)
    student.name = new_name
    student.address = new_address
    student.save()
    return HttpResponseRedirect(reverse("index"))