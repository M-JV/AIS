from django.contrib import admin

# Register your models here.
from . models import Requests
admin.site.register(Requests)

from . models import Distributor
admin.site.register(Distributor)

