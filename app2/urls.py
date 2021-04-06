from django.urls import path
from app2 import views
app_name="app2"
urlpatterns = [
    path("",views.index,name="index"),
    path("samp2/",views.samp2,name="samp1")
]