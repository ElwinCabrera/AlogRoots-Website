from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Article)
admin.site.register(Strengths)
admin.site.register(Weaknesses)
admin.site.register(Complexity)
admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(ResourcesCitations)


admin.site.register(LearnCategories)
admin.site.register(PracticeCategories)
admin.site.register(LearnCategoryItem)
admin.site.register(PracticeCategoryItem)


