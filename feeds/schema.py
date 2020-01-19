import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from feeds.models import Feed, Episode, Enclosure


# Relay
class FeedNode(DjangoObjectType):
    class Meta:
        model = Feed
        exclude = ('created_at', 'updated_at')
        filter_fields = ()
        interfaces = (graphene.relay.Node, )

    # Returns full URL from storage
    def resolve_cover(self, info):
        return self.cover.url


class EpisodeNode(DjangoObjectType):
    class Meta:
        model = Episode
        exclude = ('created_at', 'updated_at')
        filter_fields = ('feed',)
        interfaces = (graphene.relay.Node, )


class EnclosureNode(DjangoObjectType):
    class Meta:
        model = Enclosure
        exclude = ('created_at', 'updated_at')
        filter_fields = ('episode',)
        interfaces = (graphene.relay.Node, )

    def resolve_content(self, info):
        return self.content.url


class Query(graphene.ObjectType):
    feed = graphene.relay.Node.Field(FeedNode)
    all_feeds = DjangoFilterConnectionField(FeedNode)

    episode = graphene.relay.Node.Field(EpisodeNode)
    all_episodes = DjangoFilterConnectionField(EpisodeNode)

    enclosure = graphene.relay.Node.Field(EnclosureNode)
    all_enclosures = DjangoFilterConnectionField(EnclosureNode)
