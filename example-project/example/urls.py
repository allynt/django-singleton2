from django.urls import path

from example.views import IndexView

urlpatterns = [
    path("", IndexView.as_view()),
]
