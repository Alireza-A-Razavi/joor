from django.db import models
from django.contrib.contenttypes.models import (
    ContentType,
    GenericForeignKey,
    GenericRelation,
)

from joorab.apps.core.models import (
    SeoTagsBase,
    CreationModificationDateBase,
)

from .utils import products_upload_to

class Product(SeoTagsBase, CreationModificationDateBase, models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(
        upload_to=products_upload_to,
        blank=True
    )
    alt_name = models.CharField(max_length=512)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    stock = models.PostitiveIntegerField()
    ratings = Ge()
    sliders = GenericRelation(
        'SliderImage',
        related_query_name = "product_slider"
    )

    def __str__(sellf):
        return f"{self.category.title}: {self.title}"


class SliderImage(models.Model):
    image = models.ImageField(upload_to=products_upload_to)
    alt_name = models.CharField(max_length=512)
    object_id = models.PostitiveIntegerField()
    content_type = models.ForeignKey(
        "ContentType",
        on_delete=models.CASCADE
    )
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.content_object.title} slider"
