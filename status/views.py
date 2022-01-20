# from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import  mixins,ListCreateAPIView,RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import parsers, viewsets
# Create your views here.

# class StatusApiView(APIView):
#     def get(self, request, format=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)
#         return Response(status_serializer.data)

# class StatusListAPIView(mixins.CreateModelMixin, ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StatusCreateAPIView(CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get("id")
    #     return Status.objects.get(id=kw_id)

# class StatusUpdateAPIView(UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'

# class StatusDestroyAPIView(DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'


# class StatusListAPIView(ListCreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     parser_classes = [parsers.FormParser, parsers.MultiPartParser]

# class StatusDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'
#     parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

