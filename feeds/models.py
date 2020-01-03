from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    last_fetched_at = models.DateTimeField('Last fetch date')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    description = models.CharField(max_length=200)
