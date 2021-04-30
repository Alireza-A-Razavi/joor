from django.shortcuts import render
from django.views import View

from .models import MainCategory

# class MainCategotyView(View):
#
#     def get(self, request, slug, *args, **kwargs):
#         main_cat = MainCategory.objects.all()
#
#         return render(request, ,"html")
