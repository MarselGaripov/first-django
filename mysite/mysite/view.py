from django.shortcuts import render

def home(request):
    return render(request, './home.html')

def about(request):
    return render(request, './about.html')

def post_detail(request):
    return render(request, './post_detail.html')
