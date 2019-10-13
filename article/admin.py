from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Topic)
admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(GoodFor)
admin.site.register(NotGoodFor)

