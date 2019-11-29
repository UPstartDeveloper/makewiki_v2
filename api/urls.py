from django.urls import path
import api.views as api_views

app_name = 'api'
urlpatterns = [
    path('pages/', api_views.PageList.as_view(), name='wiki_list_or_create'),
    path('pages/<int:pk>/', api_views.PageOperationsView.as_view(),
         name='wiki_read_change_or_delete'),
]
