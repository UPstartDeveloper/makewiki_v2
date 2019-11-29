from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from wiki.models import Page
from api.serializers import PageSerializer


class PageList(ListCreateAPIView):
    """Presents a list of all Page objects in the database.
       Allows for the creation of new Pages.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageOperationsView(RetrieveUpdateDestroyAPIView):
    """Allows for reading, changing, or deleting a single Page instance.
       Work with GET, PUT, PATCH, or DELETE methods.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
