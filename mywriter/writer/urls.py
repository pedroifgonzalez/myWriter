from django.urls import path
from .views import index, showWritings
from django.urls import include, path
from rest_framework import routers
from writer.api import views

router = routers.DefaultRouter()
router.register(r'writings', views.WritingViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('writings/', showWritings, name='showWritings'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]