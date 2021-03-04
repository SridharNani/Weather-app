from django.urls import path,include

from weather import views
from .views import *

urlpatterns=[
    path('',views.home,name='home')
]