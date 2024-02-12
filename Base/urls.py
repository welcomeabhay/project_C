from django.urls import path
from Base import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about',views.About,name='about'),
    path('contact',views.Contact,name='contact'),
    path('category',views.CategorY,name='category'),
    path('sub_category/<str:cname>/',views.Sub_CategorY,name='sub_category'),

]
