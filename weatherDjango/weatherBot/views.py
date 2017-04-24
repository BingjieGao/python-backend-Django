from django.shortcuts import render
# api_view: http://www.django-rest-framework.org/api-guide/views/#api_view
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response

#home api_view
@api_view()
def home(request):
    return Response({"message": "Hello, world!"})
