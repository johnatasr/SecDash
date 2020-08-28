from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from hosts.views import HostsViewSet
from vulnerabilities.views import VulnerabilitiesViewSet
from app.views import IndexView

router = DefaultRouter()
router.register('hosts', HostsViewSet, basename='host')
router.register('vulnerabilities', VulnerabilitiesViewSet, basename='vulnerabilities')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('users/', include('users.urls', namespace='users')),
    path('', IndexView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
