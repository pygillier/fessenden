# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Feed
from .services import FetchFeedService


class ImportFeedForm(ModelForm):
    class Meta:
        model = Feed
        fields = ('feed_url',)

    def save(self):
        feed = FetchFeedService.execute({
            'feed_url': self.cleaned_data['feed_url']
            })

        return feed
