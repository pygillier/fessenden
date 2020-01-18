from django.forms import ModelForm
from .models import Feed


class ImportFeedForm(ModelForm):
    class Meta:
        model = Feed
        fields = ('feed_url',)