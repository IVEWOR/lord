from django.contrib import admin

from news_app.models import Author, News, NewsCategory, NewsComment

admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(NewsComment)
admin.site.register(Author)
