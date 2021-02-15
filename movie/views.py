from django.shortcuts import render
from .models import Film
import logging

logger = logging.getLogger(__name__)
def index(request):
    films = Film.objects.all()
    return render(request, 'movie/base_films_list.html', {'films': films})