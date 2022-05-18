from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.all()

    return render(request, "blogapp/home.html", {"blogs":blogs})
