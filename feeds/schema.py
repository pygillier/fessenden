# -*- coding: utf-8 -*-
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation, Field
from graphql_relay.node.node import from_global_id

from feeds.models import Feed, Episode, Enclosure
from feeds.forms import ImportFeedForm


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


# Mutations
class ImportFeedMutation(DjangoModelFormMutation):
    feed = Field(FeedNode)

    class Meta:
        form_class = ImportFeedForm


class DeleteFeed(graphene.Mutation):
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        (obj_type, obj_id) = from_global_id(kwargs["id"])
        if obj_type == "FeedNode":
            feed = Feed.objects.get(pk=obj_id)
            feed.delete()

            return cls(ok=True)
        else:
            return cls(ok=False, message="Wrong type given")


class Mutations(graphene.ObjectType):
    import_feed = ImportFeedMutation.Field()
    delete_feed = DeleteFeed.Field()
