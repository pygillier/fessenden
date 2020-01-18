from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from service_objects.views import ServiceView
from .forms import ImportFeedForm
from .services import FetchFeedService
from .models import Feed


class ImportFeedView(ServiceView):
    template_name = 'feeds/import.html'
    form_class = ImportFeedForm
    service_class = FetchFeedService
    success_url = reverse_lazy('feeds:imported')


class FeedsListView(ListView):
    model = Feed
    context_object_name = "feeds"


class FeedView(DetailView):
    model = Feed
    context_object_name = "feed"


class ImportedView(TemplateView):
    template_name = "feeds/imported.html"


class FeedDeleteView(DeleteView):
    model = Feed
    success_url = reverse_lazy('feeds:list')
