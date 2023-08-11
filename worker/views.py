from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Worker, Unit, Visit
from .serializers import UnitSerializer, VisitSerializer

class UnitsByWorkerListView(generics.ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone', None)
        if phone_number is not None:
            worker = Worker.objects.filter(phone=phone_number).first()
            if worker:
                return Unit.objects.filter(worker=worker)
        return Unit.objects.none()

class MakeVisitView(APIView):
    def post(self, request, format=None):
        unit_pk = request.data.get('unit_pk')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            unit = Unit.objects.get(pk=unit_pk)
        except Unit.DoesNotExist:
            return Response({'error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)

        visit = Visit.objects.create(unit=unit, latitude=latitude, longitude=longitude)
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
