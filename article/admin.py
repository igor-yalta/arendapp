from django.contrib import admin
from article.models import Article, FIO, Foto


# Register your models here.
class ArticleInLine(admin.StackedInline):
    model = Foto
    extra=3

#class ArticleInLine(admin.StackedInline):
#    model = FIO


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title','article_text','article_date', 'article_cover']
    inlines = [ArticleInLine]
    list_filter = ['article_date']

class FIOAdmin(admin.ModelAdmin):
    fields = ['name', 'family', 'adress', 'tel','email','fio_article']

admin.site.register(Article, ArticleAdmin)
admin.site.register(FIO, FIOAdmin)