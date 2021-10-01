from django.contrib import admin

from polls.models import User
from .models import *
admin.site.register(User)
