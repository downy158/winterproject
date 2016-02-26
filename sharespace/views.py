from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

def list(request, space_type):
    space_list = Space.objects.filter(space_type=space_type)
    space_choice = Space.SPACE_TYPE_CHOICES
    korean_space_type = Space.space_type_to_korean(space_type)
    return render(request, 'sharespace/list.html', {'space_list': space_list,
                                                    'space_type': space_type,
                                                    'space_choice': space_choice,
                                                    'korean_space_type': korean_space_type})

def detail(request, space_id):
    space = Space.objects.get(pk=space_id)
    space_choice = Space.SPACE_TYPE_CHOICES
    """ 참고 https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.get_FOO_display"""
    korean_space_type = space.get_space_type_display()
    return render(request, 'sharespace/detail.html', {'space': space,
                                                      'space_choice': space_choice,
                                                      'korean_space_type': korean_space_type})
