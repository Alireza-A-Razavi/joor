import os

from django.utils.timezone import now as timezone_now

def upload_to(instance, filename, obj_type=None):
    now = timezone_now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f"{obj_type}/{now:%Y/%m}/{instance.pk}{extension}"
