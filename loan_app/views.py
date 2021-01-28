from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def start(request):
    return render(request, 'apply.html')

def apply(request):
    return render(request, 'apply2.html')

def approve(request):
    return render(request, 'result.html')