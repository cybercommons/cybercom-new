from django.urls import include, path, re_path
from rest_framework import routers
#from tutorial import views
from django.contrib import admin
from .views import APIRoot ,UserProfile
from django.utils.translation import ugettext_lazy as _
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .jwt_payload import MyTokenObtainPairView

#JWT Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api import config


admin.site.site_header = _(config.APPLICATION_TITLE)
admin.site.site_title = _(config.APPLICATION_TITLE)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Root API
    path("",APIRoot.as_view()),
    #Authentication and Admin
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/token/$', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    # Cybercommons Django Apps
    path('queue/', include('cybercom_queue.urls')),
    path('data_store/',include('data_store.urls')),
    path('catalog/',include('catalog.urls')),
    path('user/',UserProfile.as_view(),name='user-list'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'jsonp', 'xml', 'yaml'])


