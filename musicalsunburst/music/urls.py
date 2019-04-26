from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:release_id>/', views.detail, name='detail')
##        path('AJAX', views.restReq, name='api')
]
