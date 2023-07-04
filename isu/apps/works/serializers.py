from rest_framework import serializers

from apps.works.models import Work, WorkImage
from apps.users.serializers import UserSerializer

class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    images = WorkImageSerializer(many=True, required=False)
    user = UserSerializer()
    upload_images = serializers.ListField(
        child=serializers.ImageField(
            use_url=False,
            allow_empty_file=False
        ),
        write_only=True,
        required=False
    )

    class Meta:
        model = Work
        fields = "__all__"