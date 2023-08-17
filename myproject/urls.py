from django.contrib import admin
from django.urls import path, include
from crud.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
