from service_objects.services import Service
from django import forms
import datetime
import requests
import logging
from .models import Feed, Episode, Enclosure
from django.core import files
from io import BytesIO
import podcastparser
import urllib
from django_rq import job as rq_job


logger = logging.getLogger(__name__)


class FetchFeedService(Service):

    feed_url = forms.URLField()

    def process(self):
        url = self.cleaned_data['feed_url']

        # Try to load feed
        # response = requests.get(url, stream=True)
        # feed = atoma.parse_rss_bytes(response.content)

        # Podcastparser version
        feed_content = podcastparser.parse(url, urllib.request.urlopen(url), max_episodes=2)

        print(feed_content)

        if feed_content['title']:
            feed, created = Feed.objects.update_or_create(
                feed_url=url,
                defaults={
                    'title': feed_content['title'],
                    'description': feed_content['description']
                }
            )

            if created:
                # Try to download cover if present
                if feed_content['cover_url']:
                    print(f"Image {feed_content['cover_url']}!")
                    resp = requests.get(feed_content['cover_url'])
                    if resp.status_code != requests.codes.ok:
                        #  Error handling here
                        print("KO")

                    fp = BytesIO()
                    fp.write(resp.content)
                    file_name = feed_content['cover_url'].split("/")[-1]  # There's probably a better way of doing this but this is just a quick example
                    print(f"Got filename {file_name}")
                    feed.cover.save(file_name, files.File(fp))

            for episode in feed_content['episodes']:
                ep, created = Episode.objects.update_or_create(
                    guid=episode['guid'],
                    defaults={
                        'feed': feed,
                        'title': episode['title'],
                        'subtitle': episode['subtitle'],
                        'description': episode['description'],
                        'description_html': episode['description_html'] if 'description_html' in episode.keys() else "",
                        'link': episode['link'],
                        'guid': episode['guid'],
                        'total_time': episode['total_time'],
                        'published_at': datetime.datetime.fromtimestamp(episode['published'])
                    }
                )

                if created:
                    # Load enclosures
                    for enclosure in episode['enclosures']:
                        ec, created = Enclosure.objects.update_or_create(
                            url=enclosure['url'],
                            defaults={
                                'episode': ep,
                                'size': enclosure['size'] if 'size' in enclosure.keys() else 0,
                                'mime_type': enclosure['mime_type']
                            }
                        )

                        # Get media
                        import_enclosure_content.delay(enclosure=ec)

            return feed


@rq_job('enclosures')
def import_enclosure_content(enclosure):
    media = requests.get(enclosure.url)
    if media.status_code != requests.codes.ok:
        #  Error handling here
        print("KO")
    fp = BytesIO()
    fp.write(media.content)
    file_name = enclosure.url.split("/")[-1]
    enclosure.content.save(file_name, files.File(fp))
