from django.shortcuts import render
from ..gallery.models import Location,Image,Category
# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations})
