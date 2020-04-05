# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
from .models import Choices,Question

# Register your models here.
admin.site.register(Choices)

admin.site.register(Question)