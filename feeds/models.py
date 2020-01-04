from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField()
    last_fetched_at = models.DateTimeField(
        'Last fetch date',
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.url})"


class Item(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    url = models.URLField()
    guid = models.CharField(max_length=200, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
