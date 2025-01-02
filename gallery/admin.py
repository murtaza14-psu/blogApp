from django.contrib import admin
from .models import *
# Register your models here.
#Now this product model is available for use in the admin panel of the site
admin.site.register(Product)