from django.urls import path
from .views import (SiteListView, SummaryView,
                    SiteDetailView, AverageView)

urlpatterns = [
    path("", SiteListView.as_view(), name="sites"),
    path("summary/", SummaryView.as_view(), name="summary"),
    path("summary-average/", AverageView.as_view(), name="average"),
    path("sites/<int:id>", SiteDetailView.as_view(), name="detail"),
]
