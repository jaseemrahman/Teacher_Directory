from this import d
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

from teacher.models import Teacher
from .forms import CreateUserForm
from .forms import BulkUploadForm
from django.contrib import messages
import logging
import os


# Create your views here.

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('uploads') 
        else:
            messages.info(request,"username OR password is incorrect")   

    dict_form={
    }
    return render(request,'login.html',dict_form)

def register(request):

    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created succesfully for' +user)
            return redirect('uploads') 
    dict_form={
        'form':form
    }
    return render(request,'register.html',dict_form)

def logoutuser(request):
    logout(request)
    return redirect('home')    


def save_new_teachers_from_csv(file_path):
    with open(file_path, 'r') as fp:
        teachers = csv.reader(fp, delimiter=',')
        row = 0
        for teacher in teachers:
            if row==0:
                headers = teacher
                row = row + 1
            else:
                new_teacher_details = {}
                for i in range(len(headers)):
                    new_teacher_details[headers[i]] = teacher[i]

                new_teacher_details['current_class'] = Teacher.objects.get()

                # create an instance of Teacher model
                new_teacher = Teacher()
                new_teacher.__dict__.update(new_teacher_details)
                new_teacher.save()
                row = row + 1
        fp.close()

def uploadfile(request):
    return render(request,'uploads.html')    

def uploadcsv(request):
    if request.method == 'GET':
        form = BulkUploadForm()
        return render(request, 'uploads.html', {'form':form})

    try:
        form = BulkUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('uploads')
            # If file is too large
            if csv_file.multiple_chunks():
                messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(1000*1000),))
                return redirect('uploads')
            form.save()
            file_path = os.path.join(BASE_DIR, form.csv_file.url)
            save_new_teachers_from_csv(file_path)
                
    except Exception as e:
        logging.getLogger('error_logger').error('Unable to upload file. ' + repr(e))
        messages.error(request, 'Unable to upload file. ' + repr(e))
    return redirect('uploads')

