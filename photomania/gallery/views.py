from django.shortcuts import render
from .models import Category
# Create your views here.
from .models import Image, Location

def image_location(request, location):
    """
    function to filter by location
    """
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search_results.html',{"message":message,"category": searched_category})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})



def gallery(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'gallery.html', {'images': images[::-1], 'locations': locations})


