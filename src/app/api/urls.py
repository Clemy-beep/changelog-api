from django.urls import path, register_converter
from datetime import datetime

from .views import (
    GetAllChangesView, GetChangesByVersionView, PostUnversionedChangeView, PostBuildVersionView, GetWhatsNewView,
    GetAliveView, PostVersionedChangeView, GetAllBuildsView, GetChangesByDatesView
)


urlpatterns = [
    path("", GetAliveView.as_view(), name="root"),
    path("whats-new", GetWhatsNewView.as_view(), name="whats-new"),
    path("all-changes", GetAllChangesView.as_view(), name="all-changes"),
    path("all-builds", GetAllBuildsView.as_view(), name="all-builds"),
    path("changes/<str:version>", GetChangesByVersionView.as_view(), name="changes-by-version"),
    path("changes/<str:date_end>/<str:date_start>", GetChangesByDatesView.as_view(), name="changes-by-dates"),
    path("register-change", PostUnversionedChangeView.as_view(), name="register-change"),
    path("register-build", PostBuildVersionView.as_view(), name="register-build"),
    path("register-change-with-build", PostVersionedChangeView.as_view(), name="register-change-with-build"),
]