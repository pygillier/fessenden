from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from service_objects.views import ServiceView
from .forms import ImportFeedForm
from .services import FetchFeedService
from .models import Feed


class ImportFeedView(LoginRequiredMixin, ServiceView):
    template_name = 'feeds/import.html'
    form_class = ImportFeedForm
    service_class = FetchFeedService
    success_url = reverse_lazy('feeds:imported')


class FeedsListView(LoginRequiredMixin, ListView):
    model = Feed
    context_object_name = "feeds"


class FeedView(LoginRequiredMixin, DetailView):
    model = Feed
    context_object_name = "feed"


class ImportedView(LoginRequiredMixin, TemplateView):
    template_name = "feeds/imported.html"


class FeedDeleteView(LoginRequiredMixin, DeleteView):
    model = Feed
    success_url = reverse_lazy('feeds:list')
