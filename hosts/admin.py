from django.contrib import admin
from hosts.models import Host, HostsFiles

# Register your models here.


class HostAdmin(admin.ModelAdmin):
    list_filter = ['vulnerabilities']
    list_display = ['hostname', 'id', 'ip_adress',]
    search_fields = ['hostname', 'ip_adress']

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('hostname', 'ip_adress')


class HostsFilesAdmin(admin.ModelAdmin):
    list_filter = ['status', ]
    list_display = ['key', 'file', 'date', 'status']
    search_fields = ['key', ]

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('status', 'key', 'file', 'date', 'exception', 'exceptions_file')


admin.site.register(HostsFiles, HostsFilesAdmin)
admin.site.register(Host, HostAdmin)