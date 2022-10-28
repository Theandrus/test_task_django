from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Doctor, Category
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader


def main(request):
    return render(request, 'main.html')


def show_categories(request):
    categories = Category.objects.order_by('number_of_sort')
    return render(request, 'categories.html', {'categories': categories})


def show_doctors(request):
    doctors_list = Doctor.objects.order_by('number_of_sort')
    page = request.GET.get('page', 1)
    paginator = Paginator(doctors_list, 2)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)
    return render(request, 'doctors.html', {'doctors': doctors})


def doctor_detail(request, doctor_slug):
    try:
        a = Doctor.objects.get(slug=doctor_slug)
    except:
        raise Http404("The doctor has not found(")

    return render(request, 'doctor_detail.html', {'doctor': a})

