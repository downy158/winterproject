from django.shortcuts import render
from .models import Space
# Create your views here.
def main(request):
    space_list = Space.objects.all
    space_choice = Space.SPACE_TYPE_CHOICES
    return render(request, 'sharespace/main.html', {'space_list':space_list, 'space_choice': space_choice})
