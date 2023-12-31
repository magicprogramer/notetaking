from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tag)
admin.site.register(Vault)
admin.site.register(Note)
admin.site.register(Pragraph)
admin.site.register(Link)