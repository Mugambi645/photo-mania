from django.shortcuts import render

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
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any category.Please search again"
        return render(request, 'search_results.html', {"message": message})


def gallery(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'gallery.html', {'images': images[::-1], 'locations': locations})


