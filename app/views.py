# from django.shortcuts import render
#
#
# # Create your views here.
# def index(request):
#     return render(request, 'react/index.html', context=None)
#


import os
import logging
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings


class FrontendAppView(View):
    index_file_path = os.path.join(settings.BASE_DIR, 'templates', 'react', 'index.html')

    def get(self, request):
        try:
            with open(self.index_file_path) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception('Falha ao carregar template')
            return HttpResponse(
                """
                    Ops, Erro ao carregar página !
                """,
                status=501,
            )