from service_objects.services import Service
from django import forms
import atoma, requests
from .models import Feed, Item

class FetchFeedService(Service):

    url = forms.URLField()

    def process(self):
        url = self.cleaned_data['url']

        # Try to load feed
        response = requests.get(url)
        feed_content = atoma.parse_rss_bytes(response.content)

        if feed_content.title:
            feed, created = Feed.objects.update_or_create(
                url=url,
                defaults={
                    'title': feed_content.title,
                    'description': feed_content.description
                }
            )

            for item in feed_content.items:
                print(item)
                i, created = Item.objects.update_or_create(
                    guid=item.guid,
                    defaults={
                        'feed': feed,
                        'title': item.title,
                        'url': item.link,
                        'description': item.description
                    }
                )

            return feed
