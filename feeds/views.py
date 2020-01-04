from .forms import ImportFeedForm
from service_objects.views import ServiceView
from .services import FetchFeedService
from django.views.generic.list import ListView
from .models import Feed


class ImportFeedView(ServiceView):
    template_name = 'feeds/import.html'
    form_class = ImportFeedForm
    service_class = FetchFeedService
    success_url = '/thanks'


class FeedsListView(ListView):
    model = Feed
    context_object_name = "feeds"
