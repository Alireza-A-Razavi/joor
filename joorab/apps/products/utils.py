import os

from django.utils.timezone import now as timezone_now


def products_upload_to(instance, filename):
    now = timezone_now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f"products/{now:%Y/%m}/{instance.pk}{extension}"
