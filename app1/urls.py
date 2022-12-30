from django.urls import path
from app1.views import *
app_name="haipage"

urlpatterns=[
    path("hai/",hai,name="hai"),
]