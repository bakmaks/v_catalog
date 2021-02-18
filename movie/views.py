from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView

from .models import Film
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('Hello')
    films = Film.objects.all()
    return render(request, 'movie/base_films_list.html', {'films': films})


# class RedirectToMain(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         return super().get_redirect_url(*args, **kwargs)


# def redirect_to_movie(request):
#     logger.debug(request.GET)
#     return redirect('movie/film/')
