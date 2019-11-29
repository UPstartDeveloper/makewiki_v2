from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from wiki.models import Page
from api.serializers import PageSerializer


class PageList(APIView):
    def get(self, request):
        '''Render a list of all Page objects in JSON.'''
        pages = Page.objects.all()
        data = PageSerializer(pages, many=True).data
        return Response(data)
