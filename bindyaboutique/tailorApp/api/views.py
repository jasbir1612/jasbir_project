from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView

from tailorApp.api.serializers import BodyMeasurementsSerializer

from tailorApp.models import BodyMeasurements


class BodyMeasurementsList(ListAPIView):
    queryset = BodyMeasurements.objects.all()
    serializer_class = BodyMeasurementsSerializer



class BodyMeasurementsCreate(CreateAPIView):
    queryset = BodyMeasurements.objects.all()
    serializer_class = BodyMeasurementsSerializer


class BodyMeasurementsRetrieve(RetrieveAPIView):
    queryset = BodyMeasurements.objects.all()
    serializer_class = BodyMeasurementsSerializer

class BodyMeasurementsUpdate(RetrieveUpdateDestroyAPIView):
    queryset = BodyMeasurements.objects.all()
    serializer_class = BodyMeasurementsSerializer
