from django.urls import path
from .views import UnitsByWorkerListView, MakeVisitView

urlpatterns = [
    path('api/get_units/', UnitsByWorkerListView.as_view(), name='get_units'),
    path('api/make_visit/', MakeVisitView.as_view(), name='make_visit'),
]
