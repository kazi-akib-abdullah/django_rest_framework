from django.urls import path
from .views import StatusViewset
from rest_framework import routers

# status/ -> List, Create => GET, POST
# status/<id>/ -> Details, Delete, Update => GET, DELETE, PUT/PATCH
router = routers.DefaultRouter()
router.register(r'status', StatusViewset, basename="status")
urlpatterns = [
    # path('status/', StatusApiView.as_view()),
    # path('status/', StatusListAPIView.as_view()),
    # path('status/create/', StatusCreateAPIView.as_view()),
    # path('status/<id>/', StatusDetailAPIView.as_view()),
    # path('status/update/<id>/', StatusUpdateAPIView.as_view()),
    # path('status/delete/<id>/', StatusDestroyAPIView.as_view()),
]+ router.urls