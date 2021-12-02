from django.shortcuts import render
from gallery.models import Location,Image,Category
# Create your views here.
def index(request):
    return render(request, "index.html")