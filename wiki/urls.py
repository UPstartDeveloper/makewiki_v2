from django.urls import path
from wiki.views import PageListView, PageDetailView, get_page


urlpatterns = [
        path('', PageListView.as_view(), name='wiki-list-page'),
        path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
        path('create', get_page)
]
