from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from wiki.models import Page
from api.serializers import PageSerializer


class PageList(ListCreateAPIView):
    """Presents a list of all Page objects in the database.
       Allows for the creation of new Pages.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetail(RetrieveDestroyAPIView):
    """Presents a specific Page in more detail.
       Allows for deletions of a Page.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
