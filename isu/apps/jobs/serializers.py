from rest_framework import serializers

from apps.jobs.models import Job, JobImage
from apps.users.serializers import UserSerializer


class JobImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobImage
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    images = JobImageSerializer(many=True, required=False, read_only=True)
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
        model = Job
        fields = "__all__"
