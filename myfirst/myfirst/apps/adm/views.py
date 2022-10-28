from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from doctors.models import Doctor, Category


def main(request):
    return render(request, 'administration/main_adm.html')


def about_us(request):
    return render(request, 'administration/about_us.html')


def show_categories(request):
    categories = Category.objects.all()
    return render(request, 'administration/adm_categories.html', {'categories': categories})


def show_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'administration/adm_doctors.html', {'doctors': doctors})


def delete_categories(request, slug):
    a = Category.objects.filter(slug=slug).delete()
    categories = Category.objects.all()
    return render(request, 'administration/adm_categories.html', {'categories': categories})


def delete_doctors(request, slug):
    a = Doctor.objects.filter(slug=slug).delete()
    doctors = Doctor.objects.all()
    return render(request, 'administration/adm_doctors.html', {'doctors': doctors})


def add_page_categories(request):
    return render(request, 'administration/add_page_categories.html')


def add_page_doctors(request):
    return render(request, 'administration/add_page_doctors.html')


def categories_add(request):
    a = Category(category_name=request.POST['Name'], slug=request.POST['Slug'], number_of_sort=request.POST['Number_of_sort'])
    a.save()
    categories = Category.objects.all()
    return render(request, 'administration/adm_categories.html', {'categories': categories})


def doctors_add(request):
    a = Doctor(doctor_name=request.POST['doctor_name'], slug=request.POST['slug'], categories=Category.objects.get(slug=request.POST['category']),
               description=request.POST['description'], birth_date=request.POST['birth_date'],
               experience=request.POST['experience'], number_of_sort=request.POST['number_of_sort'])
    a.save()
    doctors = Doctor.objects.all()
    return render(request, 'administration/adm_doctors.html', {'doctors': doctors})


def upd_page_categories(request, slug):
    a = Category.objects.get(slug=slug)
    return render(request, 'administration/upd_page_doctors.html', {'category': a})


def categories_update(request, slug):
    a = Category.objects.filter(slug=slug).update(category_name=request.POST['Name'], slug=request.POST['Slug'],
                                                  number_of_sort=request.POST['Number_of_sort'])
    categories = Category.objects.all()
    return render(request, 'administration/adm_categories.html', {'categories': categories})





