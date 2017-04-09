from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,HyperlinkedRelatedField,SerializerMethodField
from tailorApp.models import BodyMeasurements


class BodyMeasurementsSerializer(ModelSerializer):
    class Meta:
        model = BodyMeasurements
        fields = [
        "id",
        "name",
        "due_date",
        "description",
        "length",
        "Cross_Chest",
        "Chest",
        "Waist",
        "Hipp",
        "Armhole",
        "Shoulder",
        "Neck",
        "Sleeves",
        "Salwar",
        "Mori",
        "Knee",
        "Calf",
        "Theigh",
        "BLenght",
        "BChest",
        "BShoulder",
        "BWaist",
        "BWaist",
        "BSleeves",
        "BDaat_Point",
        ]
