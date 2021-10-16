from django.urls import path
from .views import Run, Download

urlpatterns = [
    path('', Run, name='run'),
    path('download/', Download, name = 'download')
]
