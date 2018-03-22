"""This is a package for using by other parts of Coralline project.
Detailed description pending."""

import os
import django
from django.conf import settings

if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_coralline_images.settings")
    django.setup()
