from django.urls import path
import api.views as api_views

urlpatterns = [
    path('pages/', api_views.PageList.as_view(), name='wiki_list'),

]
