from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    name = 'joorab.apps.categories'
    verbose_name = _("Categories")

    def ready(self):
        from . import signals
