from django.shortcuts import render, get_object_or_404
from .models import Space
# Create your views here.
def main(request):
    space_list = Space.objects.all
    space_choice = Space.SPACE_TYPE_CHOICES
    return render(request, 'sharespace/main.html', {'space_list':space_list, 'space_choice': space_choice})

# def list(request):
#     space_list = Space.objects.all
#     space_choice = Space.SPACE_TYPE_CHOICES
#     return render(request, 'sharespace/list.html', {'space_list':space_list, 'space_choice': space_choice})

def list(request, space):
    space_list = Space.objects.all
    space_choice = Space.SPACE_TYPE_CHOICES
    space_filter = Space.objects.filter(space_type=space)
    space_type = space[0:]
    return render(request, 'sharespace/list.html', {'space_list':space_list, 'space_choice': space_choice, 'space_filter':space_filter, 'space_type':space_type})
