from rest_framework import serializers
from .models import Vulnerability

# Register your serializers here.
class VulnerabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = "__all__"
        depth = 1


class VulneGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['title', 'severity', 'cvss']
        depth = 1


class VulneOnlyIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = ['id']
        depth = 1