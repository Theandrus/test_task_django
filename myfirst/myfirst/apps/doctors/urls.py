from django.urls import path
from . import views

app_name = 'doctors'
urlpatterns = [
    path('', views.main, name='main'),
    path('categories/', views.show_categories, name='show_categories'),
    path('doctors/', views.show_doctors, name='show_doctors'),
    path('doctors/<slug:doctor_slug>/', views.doctor_detail, name='doctor_detail'),

]