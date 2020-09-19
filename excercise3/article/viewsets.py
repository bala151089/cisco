# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-02-04 22:52:38
# @Last Modified by:   Shubham Bansal
# @Last Modified time: 2018-04-24 03:37:47
from rest_framework import viewsets, filters
from .models import Router
from .serializers import RouterSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Name', 'status')
