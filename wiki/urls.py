from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreate


urlpatterns = [
        path('', PageListView.as_view(), name='wiki-list-page'),
        path('<str:slug>', PageDetailView.as_view(), name='wiki-details-page'),
        path('create/', PageCreate.as_view(), name="create_page_form")
]
