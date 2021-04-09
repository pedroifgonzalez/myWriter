from django.urls import path
from .views import index, showWritings

urlpatterns = [
    path('', index, name='index'),
    path('writings/', showWritings, name='showWritings'),
]