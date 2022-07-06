from django.shortcuts import render,redirect
from .models import Teacher

# from .forms import UserForm
# from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    dict_teacher={
'teacher':Teacher.objects.all()
    }
    return render(request,'index.html',dict_teacher)

def detail(request,id):
    dict_detail={
'dtl':Teacher.objects.get(pk=id)
    }
    return render(request,'detail.html',dict_detail)

