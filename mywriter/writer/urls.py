from django.urls import include, path
from writer.views import index, showWritings

urlpatterns = [
    path('', index, name='index'),
    path('writings/', showWritings, name='showWritings'),
]