from rest_framework import serializers
from Fake_Profile_Detection_Matrimony.models import AdminPanel, UserCheck


class AdminPanelSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField()
    is_superuser = serializers.SerializerMethodField()

    def get_is_superuser(self, obj):
        return getattr(obj, 'is_superuser', True)

    def get_is_admin(self, obj):
        return getattr(obj, 'is_admin', True)

    class Meta:
        model = AdminPanel
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminPanel
        fields = "__all__"


class UserCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCheck
        fields = "__all__"
