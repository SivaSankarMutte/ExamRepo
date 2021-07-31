from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
#EMAIL concept
from cricbuzz import settings
from django.core.mail import send_mail
import random

def home(request):
	return render(request,'ht1/home.html')
