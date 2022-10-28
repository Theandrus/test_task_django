from django.urls import path
from . import views

app_name = 'adm'
urlpatterns = [
    path('', views.main, name='main'),
    path('about_us/', views.about_us, name='about_us'),
    path('categories/', views.show_categories, name='show_categories'),
    path('doctors/', views.show_doctors, name='show_doctors'),
    path('categories/<slug:slug>/delete', views.delete_categories, name='delete_categories'),
    path('doctors/<slug:slug>/delete', views.delete_doctors, name='delete_doctors'),
    path('doctors/add', views.add_page_doctors, name='add_doctors'),
    path('categories/add', views.add_page_categories, name='add_categories'),
    path('categories/add/create', views.categories_add, name='categories_add'),
    path('doctors/add/create', views.doctors_add, name='doctors_add'),
    path('categories/<slug:slug>/update', views.upd_page_categories, name='upd_page_categories'),
    path('categories/<slug:slug>/update/change', views.categories_update, name='categories_update'),

]