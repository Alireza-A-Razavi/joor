from django.shortcuts import render
from django.views import View

from joorab.apps.categories.models import MainCategory
# from joorab.apps.products.models import MainCategory


class IndexView(View):

    def get(self, request, *args, **kwargs):
        main_cats = MainCategory.objects.all()

        context = {
            "main_cats": main_cats
        }

        return render(request, "index.html", context)
