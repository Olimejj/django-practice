from django.urls import path
from . import views

# URLConf module
urlpatterns = [
    path('hello/', views.say_hello),
    path('entryform/', views.display_form)
        ]
