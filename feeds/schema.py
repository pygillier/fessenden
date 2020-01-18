import graphene
from graphene_django.types import DjangoObjectType
from feeds.models import Feed, Episode


class FeedType(DjangoObjectType):
    class Meta:
        model = Feed


class EpisodeType(DjangoObjectType):
    class Meta:
        model = Episode


class Query(object):
    all_feeds = graphene.List(FeedType)
    all_episodes = graphene.List(EpisodeType)

    def resolve_all_feeds(self, info, **kwargs):
        return Feed.objects.all()

    def resolve_all_episodes(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Episode.objects.select_related('feed').all()
