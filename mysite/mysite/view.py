from django.shortcuts import render

def home(request):
    return render(request, './home.html')

def about(request):
    return render(request, './about.html')

def post_detail(request, post_id):
    return render(request, './post_detail.html', {'post_id': post_id})

def reviews(request):
    return render(request, './reviews.html')