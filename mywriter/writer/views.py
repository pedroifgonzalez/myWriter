from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from .models import Writing

INTRODUCTION = 'Welcome to myWriter! A web app based on python framework Django \
                and inspired by the online typewriter Writer. Designed to be simple \
                to use and nice for the eyes.'
TITLE_PLACEHOLDER = 'Put your title here'
BODY_PLACEHOLDER = 'Write without distractions'

def index(request):
    return render(request,'login.html')

def showWritings(request):
    username = request.POST.get('author')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user:
        login(request, user)
        values_for_template = {}
        writings = Writing.objects.all().order_by('creation_date').reverse()

        values_for_template['title_placeholder'] = TITLE_PLACEHOLDER
        values_for_template['body_placeholder'] = BODY_PLACEHOLDER
        values_for_template['writings'] = writings
        values_for_template['introduction'] = INTRODUCTION

        return render(request,'writings_list.html', values_for_template)
    
    else:
        raise PermissionDenied