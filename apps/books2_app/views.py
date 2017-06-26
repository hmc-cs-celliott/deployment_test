import time
import random
from django.shortcuts import render, HttpResponse, redirect
from.models import Course, Description
from django.contrib import messages

def index(request):
	context = {
		'courses':Course.objects.all()
	}
	return render(request, "books2_app/index.html", context) 

def add_course(request):
	result = Course.objects.create(name=request.POST['name'])
	print result
	#new_course = Course.objects.get(id=result)
	#print new_course
	Description.objects.create(description=request.POST['description'], course=result)
	return redirect('/')

def delete_course(request, id):
	result = Course.objects.get(id=id)
	print result
	result.description.delete()
	result.delete()
	return redirect('/')