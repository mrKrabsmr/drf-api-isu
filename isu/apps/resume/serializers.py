from rest_framework import serializers

from apps.resume.models import Resume, ResumeImage
from apps.users.serializers import UserSerializer


class ResumeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeImage
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    images = ResumeImageSerializer(many=True, required=False, read_only=True)
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
        model = Resume
        fields = "__all__"


    