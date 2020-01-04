from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path('import/', views.ImportFeedView.as_view(), name='import'),
    path('list/', views.FeedsListView.as_view(), name='list')
]
