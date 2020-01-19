from django.db import models
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from djchoices import ChoiceItem, DjangoChoices
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Upload locations
def feed_cover_location(instance, filename):
    return 'feeds/{0}/cover/{1}'.format(
        instance.id,
        filename)


def feed_enclosure_location(instance, filename):
    return 'feeds/{0}/episodes/{1}'.format(
        instance.episode.feed.id,
        filename)


class Feed(models.Model):
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    cover = ThumbnailerImageField(
        upload_to=feed_cover_location,
        null=True,
        blank=True)
    link = models.URLField()
    feed_url = models.URLField()
    last_fetched_at = models.DateTimeField(
        'Last fetch date',
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.url})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Feed, self).save(*args, **kwargs)


class Episode(models.Model):
    feed = models.ForeignKey(
        Feed,
        on_delete=models.CASCADE,
        related_name='episodes')

    class Status(DjangoChoices):
        unplayed = ChoiceItem('unplayed', 'Unplayed')
        ongoing = ChoiceItem('ongoing', 'Ongoing')
        finished = ChoiceItem('finished', 'Finished')

    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_html = models.TextField(blank=True)

    published_at = models.DateTimeField()
    link = models.URLField()
    total_time = models.IntegerField(default=0)
    guid = models.CharField(max_length=200, unique=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.unplayed
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']


class Enclosure(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='enclosures')

    url = models.URLField(unique=True)
    size = models.IntegerField(default=0)
    mime_type = models.CharField(max_length=36, blank=True)

    content = models.FileField(
        upload_to=feed_enclosure_location,
        null=True,
        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Deletion signals
@receiver(post_delete, sender=Enclosure)
def enclosure_content_delete(sender, instance, **kwargs):
    instance.content.delete(False)


@receiver(post_delete, sender=Feed)
def feed_cover_delete(sender, instance, **kwargs):
    instance.cover.delete_thumbnails()
    instance.cover.delete(False)
