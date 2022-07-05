from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news_app.models import Author, News, NewsCategory, NewsComment


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(NewsCategory)
class NewsCategoryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


@admin.register(Author)
class NewsAuthorAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(NewsComment)
