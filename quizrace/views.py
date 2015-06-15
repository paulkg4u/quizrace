from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators impor login_required
from django.contrib.auth.models import User
import os
import json
from quizrace.models import *


def landing(request):
	return render(request,'quizrace/landing.html')

#@login_required
def home(request):
	return render(request,'quizrace/home.html')