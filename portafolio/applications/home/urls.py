from unicodedata import name
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home",),
    path('contact', views.ContactCreateView.as_view(), name='add-contact',), 
    path('detail/<pk>', views.DetailProjectView.as_view(), name='detail-project',), 
]



