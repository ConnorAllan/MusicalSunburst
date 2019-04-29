from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('AJAX', views.restReq, name='api'),
        path('aboutus', views.aboutus, name='aboutus')
]
