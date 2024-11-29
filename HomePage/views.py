from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "HomePage/homepage-old.html")


def projects(request, id):
    return render(request, f"Projects/project{id}-old.html")


