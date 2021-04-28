from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

class SeoTagsBase(models.Model):
    meta_description = models.CharField(max_length=248)
    canonical_rel = models.CharField(max_length=16384)
    meta_author = models.CharField(max_length=225)
    meta_copyright = models.CharField(max_length=225)
    title_tag = models.CharField(max_length=68)

    class Meta:
        abstract = True

    def get_meta_tags(self, *args, **kwargs):
        pass # COMBAK: create the method to return tags in html



class CreationModificationDateBase(models.Model):
    create_at = models.DateTimeField(
        _("تاریخ تولید "),
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        _("تاریخ تغییر"),
        auto_now=True
    )

    class Meta:
        abstract = True
