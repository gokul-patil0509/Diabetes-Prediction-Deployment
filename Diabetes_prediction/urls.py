
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
     path('', include('Classifier_Web_App.urls')),
]
