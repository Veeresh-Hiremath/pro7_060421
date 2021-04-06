from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path("",views.index,name="index"),
    path("samp1/",views.samp1,name="samp1"),
    path("fact/<num>",views.facto,name="fact"),
    path("add/<num1>/<num2>",views.add,name="add"),
    path("<data>/",views.carry_data,name="data")
]
