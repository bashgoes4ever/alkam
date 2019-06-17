from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = [field.name for field in Article._meta.fields]

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)