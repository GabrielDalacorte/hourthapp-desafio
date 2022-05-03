from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from hourthapp.api.serializers import HourthAppSerializer
from hourthapp.models import HourthApp


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = HourthApp.objects.all()
    serializer_class = HourthAppSerializer
