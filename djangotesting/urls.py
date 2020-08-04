from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from djangotesting.api.views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
