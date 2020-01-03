import graphene
from graphene_django.types import DjangoObjectType
from feeds.models import Feed, Item


class FeedType(DjangoObjectType):
    class Meta:
        model = Feed


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(object):
    all_feeds = graphene.List(FeedType)
    all_items = graphene.List(ItemType)

    def resolve_all_feeds(self, info, **kwargs):
        return Feed.objects.all()

    def resolve_all_items(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Item.objects.select_related('feed').all()
