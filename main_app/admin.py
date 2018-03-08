from django.contrib import admin
from .models import Site, Test_details, Variation, Acubox







# Register your models here.
admin.site.register([Site, Test_details, Variation, Acubox])