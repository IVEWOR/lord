from django.db import models


# Authors
class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    # image -- pending
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "news_authors"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["name"]

    def __str__(self):
        return self.name


# News Categories
class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "news_categories"
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


# News
class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    # featured_image -- pending
    news_category = models.ForeignKey(
        NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "news_posts"
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


# News Comments
class NewsComment(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "news_comments"
        verbose_name = "News Comment"
        verbose_name_plural = "News Comments"
        ordering = ["-created_at"]

    def __str__(self):
        return self.comment + " - " + self.name
