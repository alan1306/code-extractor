from django.urls import path
from . import views
app_name='homePage'
urlpatterns= [
    path('',views.home,name='home'),
    path('result/',views.result,name='result'),
]

