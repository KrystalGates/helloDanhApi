"""helloDanh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from helloDanhApi.views import register_user, login_user
from helloDanhApi.views import Alerts
from helloDanhApi.views import CustomUsers
from helloDanhApi.views import UserViewSet
from helloDanhApi.views import Contacts

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customusers', CustomUsers, 'customuser')
router.register(r'users', UserViewSet, 'user')
router.register(r'contacts', Contacts, 'contact')
router.register(r'alerts', Alerts, 'alert')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
