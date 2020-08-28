from django.contrib import admin
from vulnerabilities.models import Vulnerability
# Register your models here.


class VulneAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'severity', 'cvss', 'publication_date', 'corrected']
    search_fields = ['id', 'title', 'severity']

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('title', 'severity', 'cvss', 'publication_date',)

admin.site.register(Vulnerability, VulneAdmin)