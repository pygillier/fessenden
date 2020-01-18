from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path('import/', views.ImportFeedView.as_view(), name='import'),
    path('', views.FeedsListView.as_view(), name='list'),
    path('imported/', views.ImportedView.as_view(), name='imported'),
    path('v/<slug:slug>/', views.FeedView.as_view(), name='detail'),
    path('d/<slug:slug>/', views.FeedDeleteView.as_view(), name='delete'),
]
