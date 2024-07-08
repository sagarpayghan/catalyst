from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CompanyModel
from .serializer import CompanySerializer
from .forms import MyUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pandas as pd
from sqlalchemy import create_engine
import os
from store_sql import toSQL
from django.db.models import Q

# Create your views here.
@login_required(login_url="/accounts/login/",redirect_field_name="")
def query_view(request):
    return render(request,'catalyst_count_app/querydata.html')

@login_required(login_url="/accounts/login/",redirect_field_name="")
def upload_view(request):
    
    return render(request,'catalyst_count_app/upload.html')

@login_required(login_url="/accounts/login/",redirect_field_name="")
def user_view(request):
    users= User.objects.all()
    return render(request,'catalyst_count_app/users.html',{"users":users})

@login_required(login_url="/accounts/login/",redirect_field_name="")
def create_user(request):
    form=MyUserForm()
    if request.method=="POST":
        form=MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User added successfully")
            form=MyUserForm()
    return render(request,"catalyst_count_app/create.html",{"form":form})

@login_required(login_url="/accounts/login/",redirect_field_name="")
def delete_user(request,id):
    if request.method=="POST":
        p=User.objects.get(pk=id)
        p.delete()
        messages.success(request,"User deleted successfully")
        return redirect("userspage")

@api_view(["GET"])
def getData(request):
    q=Q(City='Mumbai') | Q(state='Maharashtra')
    companies_data=CompanyModel.objects.filter(q)
    serialized=CompanySerializer(companies_data,many=True)
    return Response(serialized.data)

@api_view(["POST"])
def postData(request):
    myfile= request.FILES.get('myfile')
    if myfile:
        if myfile.multiple_chunks():
            with open("media/data.csv",'ab') as d:
                for chunk in myfile.chunks():
                    d.write(chunk)
            toSQL()
        else:
            print("save direct")
    return Response("csv uploaded in Database")
