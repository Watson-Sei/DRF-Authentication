from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('message', views.MessageViewSet)

app_name='apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('hello/',views.HelloView.as_view(),name='hello'),
]