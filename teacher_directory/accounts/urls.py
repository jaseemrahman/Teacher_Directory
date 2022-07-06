
from django.urls import path,include
from .import views
urlpatterns = [
    path('login',views.loginpage,name='login'),
    path('register',views.register,name='register'),
    path('uploads',views.uploadfile,name='uploads'),
    path('logout',views.logoutuser,name='logout'),
]