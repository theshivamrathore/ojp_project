from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index_view(request):
    return  render(request, "jobApp/index.html")

def register_view(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_number = request.POST.get('mobile_number')
        user_name = request.POST.get('user_name')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        Data = Registration_model(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
            user_name=user_name,
            email_id=email_id,
            password=password,
            confirm_password=confirm_password
        )

        Data.save()
        return render(request,'jobApp/register.html')
    else:
        return render(request,'jobApp/register.html')



def login_view(request):
    return render(request,'jobApp/login.html')

def govtjob_views(request):
    gdata = Govtjob_detail_model.objects.all()
    context = {'gdata':gdata}
    return render(request, 'jobApp/govtjob.html',context=context)