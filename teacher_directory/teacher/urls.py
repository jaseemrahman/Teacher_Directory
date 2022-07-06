
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('teacher/<int:id>',views.detail,name='details'),
]
