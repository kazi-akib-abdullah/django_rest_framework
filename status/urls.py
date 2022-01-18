from django.urls import path
from .views import StatusApiView, StatusListAPIView, StatusCreateAPIView, StatusDetailAPIView, StatusUpdateAPIView, StatusDestroyAPIView
urlpatterns = [
    path('status/', StatusApiView.as_view()),
    path('status/list/', StatusListAPIView.as_view()),
    path('status/create/', StatusCreateAPIView.as_view()),
    path('status/detail/<id>', StatusDetailAPIView.as_view()),
    path('status/update/<id>', StatusUpdateAPIView.as_view()),
    path('status/delete/<id>', StatusDestroyAPIView.as_view()),
]