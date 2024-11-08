from django.urls import path
from . import views

urlpatterns = [

    path('', views.preeclampsia, name='preeclampsia1'),
    path('base/', views.base, name='base'),
    # path('users/correlation/', views.correlation, name='correlation'),

]