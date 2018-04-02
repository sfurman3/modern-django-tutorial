from django.conf.urls import url, include
from rest_framework import routers
from project.api import views

from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

schema_view = get_schema_view(title='Users API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', schema_view)
]
