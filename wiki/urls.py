from django.urls import path
from wiki.views import PageListView, PageDetailView, CreatePageForm


urlpatterns = [
        path('', PageListView.as_view(), name='wiki-list-page'),
        path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
        path('create', CreatePageForm.as_view(), name="create_page_form")
]
