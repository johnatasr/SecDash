from rest_framework import serializers
from .models import Host, HostsFiles

# Register your serializers here.
class HostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = "__all__"
        depth = 1

class HostsFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostsFiles
        fields = "__all__"
        depth = 1





