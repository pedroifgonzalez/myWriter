from django.urls import include, path
from writer.views import index

urlpatterns = [
    path('', index, name="index"),
]