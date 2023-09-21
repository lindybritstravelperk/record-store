from django.urls import path

from . import views

app_name = "artists"

urlpatterns = [
    path("", views.Artists.as_view()),
    path("<int:pk>", views.ArtistDetail.as_view()),
]
