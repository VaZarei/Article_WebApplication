from django.contrib import admin
from .models import ArticleDB, Comments
# Register your models here.



class CommnetInLine(admin.StackedInline):
    model = Comments
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommnetInLine]


admin.site.register(ArticleDB, ArticleAdmin)
admin.site.register(Comments)