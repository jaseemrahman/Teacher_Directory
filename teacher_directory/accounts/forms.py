from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from .models import BulkUpload


class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','first_name','last_name']

class BulkUploadForm(forms.ModelForm):
  class Meta:
    model = BulkUpload
    fields = ("csv_file",)        