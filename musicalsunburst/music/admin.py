from django.contrib import admin
from .models import Releases
from .models import Songs
from .models import Artists

# Register your models here.

admin.site.register(Releases)
admin.site.register(Songs)
admin.site.register(Artists)
