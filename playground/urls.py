from django.urls import path
from . import views

#URLlConf
urlpatterns = [
    path('hello/', views.say_hello)
]
