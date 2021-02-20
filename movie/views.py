from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView

from .models import Film
import logging

logger = logging.getLogger(__name__)


def index(request):
    # logger.debug('Hello')
    films = Film.objects.all()
    return render(request, 'movie/cards_list.html', {'films': films})


# def redirect_to_movie(request):
#     logger.debug(request.GET)
#     return redirect('movie/film/')
