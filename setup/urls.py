from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from prescriptions.views import PrescriptionsViewSet

router = routers.DefaultRouter()
router.register('prescriptions',PrescriptionsViewSet, basename = 'prescriptions' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
