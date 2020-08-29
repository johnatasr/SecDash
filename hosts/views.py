from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_406_NOT_ACCEPTABLE, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from django.core.paginator import Paginator
from .models import Host, HostsFiles
from vulnerabilities.models import Vulnerability
from vulnerabilities.serializers import VulneGraphSerializer
from .serializers import HostsSerializer, HostsFilesSerializer
from .filters import data_csv_tratament, get_severity_by_media
from datetime import datetime
import random
import string
import pandas as pd
from django.conf import settings


# Register your viewsets here.
class HostsViewSet(viewsets.ModelViewSet):
    queryset = []

    @action(methods=['GET'], detail=False)
    def list_hosts(self, request):
        try:
            page = request.query_params.get('page')
            queryset = Host.objects.filter(vulnerabilities__corrected=False).order_by('hostname').distinct()
            serializer = HostsSerializer(queryset, many=True).data

            hosts = Paginator(serializer, 50)
            page_hosts = hosts.page(page)

            list_hosts = []
            for host in page_hosts.object_list:
                list_hosts.append(host)

            return Response({"hostsList": list_hosts}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar Hosts', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def list_hosts_per_row(self, request):
        try:
            queryset = Host.objects.filter(vulnerabilities__corrected=False).order_by('hostname').distinct()
            serializer = HostsSerializer(queryset, many=True).data

            list_total = []
            for host in serializer:
                for vulne in host['vulnerabilities']:

                    date = vulne['publication_date'].split('-')

                    payload = {
                        'hostname': host['hostname'],
                        'ip_adress': host['ip_adress'],
                        'title': vulne['title'],
                        'severity': vulne['severity'],
                        'cvss': vulne['cvss'],
                        'publication_date': datetime(int(date[0]), int(date[1]), int(date[2][:2])).strftime('%d/%m/%Y')
                    }
                    list_total.append(payload)

            return Response({"hostsList": list_total}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar Hosts', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def filter_hosts_per_row(self, request):
        try:
            title = request.query_params.get('vulnerabilityTitle')

            queryset = Host.objects.filter(
                vulnerabilities__corrected=False,
                vulnerabilities__title__istartswith=title
            ).order_by('hostname')

            vulne_ids = Host.objects.filter(
                vulnerabilities__corrected=False,
                vulnerabilities__title__istartswith=title
            ).values('vulnerabilities__id')

            list_ids_vulnes = []
            for id in vulne_ids:
                list_ids_vulnes.append(id['vulnerabilities__id'])

            serializer = HostsSerializer(queryset, many=True).data
            aux = 0
            list_total = []
            for host in serializer:
                for vulne in host['vulnerabilities']:
                    if int(vulne['id']) in list_ids_vulnes:
                        date = vulne['publication_date'].split('-')

                        payload = {
                            'hostname': host['hostname'],
                            'ip_adress': host['ip_adress'],
                            'title': vulne['title'],
                            'severity': vulne['severity'],
                            'cvss': vulne['cvss'],
                            'publication_date': datetime(int(date[0]), int(date[1]), int(date[2][:2])).strftime('%d/%m/%Y')
                        }
                        list_total.append(payload)
                    else:
                        del vulne
                    aux = aux + 1

            return Response({"hostsList": list_total}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar Hosts', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def filter_hosts(self, request):
        page = request.query_params.get('page')
        title = request.query_params.get('vulnerabilityTitle')

        get_vulnes = Vulnerability.objects.filter(title__istartswith=title, corrected=False).values('id')

        if not get_vulnes.exists():
            return Response([], status=HTTP_200_OK)

        if get_vulnes.exists():
            vulne_ids_list = []
            for vulne in get_vulnes:
                vulne_ids_list.append(vulne['id'])
        else:
            return Response('Nenhum Host encontrado ! ', status=HTTP_204_NO_CONTENT)

        queryset = Host.objects.filter(vulnerabilities__id__in=vulne_ids_list)

        if not queryset.exists():
            return Response('Nenhum Host encontrado ! ', status=HTTP_204_NO_CONTENT)

        serializer = HostsSerializer(queryset, many=True).data
        hosts = Paginator(serializer, 50)
        page_hosts = hosts.page(page)

        list_hosts = []
        for host in page_hosts.object_list:
            list_hosts.append(host)

        return Response({"hostsList": list_hosts}, status=HTTP_200_OK)

    @action(methods=['GET'], detail=False)
    def detail_host(self, request):
        try:
            host_id = request.query_params.get('id')
            queryset = Host.objects.filter(id=host_id)
            serializer = HostsSerializer(queryset, many=True).data

            return Response({"host": serializer}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Não é possivel carregar o Host solicitado', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def get_cards(self, request):
        try:
            total_hosts = Host.objects.all()
            total_vulne = Vulnerability.objects.all()

            if total_vulne.count() < 10:
                return Response([], status=HTTP_200_OK)

            total_vulne_host = total_hosts.distinct('hostname')\
                .filter(vulnerabilities__corrected=False).count()

            not_corrected = total_vulne.filter(corrected=False).count()
            queryset = total_vulne.values('cvss')

            list_cvss = []
            for cvss in queryset:
                list_cvss.append(cvss['cvss'])

            media = sum(list_cvss) / len(list_cvss)
            severity = get_severity_by_media(media)

            payload = {
                "totalVulnerabilities": total_vulne.count(),
                "notCorrected": not_corrected,
                "totalHosts": total_hosts.count(),
                "totalHostsVulne": total_vulne_host,
                "mediaCVSS": str(round(media, 2)),
                "severity": severity
            }
            return Response(payload, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar dados', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def get_graphics(self, request):
        try:
            total_vulnes = Vulnerability.objects.all().count()
            if total_vulnes < 10:
                return Response([], status=HTTP_200_OK)

            severity_low = Vulnerability.objects.filter(severity__istartswith='Baixo', corrected=False)\
                .values('title', 'severity', 'cvss').distinct('title')
            severity_medium = Vulnerability.objects.filter(severity__istartswith='Médio', corrected=False)\
                .values('title', 'severity', 'cvss').distinct('title')
            severity_high = Vulnerability.objects.filter(severity__istartswith='Alto', corrected=False)\
                .values('title', 'severity', 'cvss').distinct('title')
            severity_critical = Vulnerability.objects.filter(severity__istartswith='Crítico', corrected=False)\
                .values('title', 'severity', 'cvss').distinct('title')

            severity_low_serializer = VulneGraphSerializer(severity_low, many=True).data
            severity_medium_serializer = VulneGraphSerializer(severity_medium, many=True).data
            severity_high_serializer = VulneGraphSerializer(severity_high, many=True).data
            severity_critical_serializer = VulneGraphSerializer(severity_critical, many=True).data

            payload = {
                "severitylow": severity_low_serializer,
                "severityMedium": severity_medium_serializer,
                "severityHigh": severity_high_serializer,
                "severityCritical": severity_critical_serializer,
            }
            return Response(payload, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar dados', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def get_top_ten(self, request):
        try:
            total_vulnes = Vulnerability.objects.all().count()
            if total_vulnes < 10:
                return Response([], status=HTTP_200_OK)

            queryset = Host.objects.all().order_by('hostname')
            serializer = HostsSerializer(queryset, many=True).data

            for host in serializer:
                list_cvss = []
                for vulne in host['vulnerabilities']:
                    list_cvss.append(float(vulne['cvss']))

                media = sum(list_cvss) / len(list_cvss)
                severity = get_severity_by_media(media)
                host['cvssTotal'] = str(round(media, 2))
                host['severity'] = severity
                del host['vulnerabilities']

            top_ten_list = sorted(serializer, reverse=True, key=lambda key_value_pair: key_value_pair['cvssTotal'])[:10]

            return Response({"topTen": top_ten_list}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar dados', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['POST'], detail=False)
    def import_csv_file(self, request):

        if 'file' not in request.data:
            raise ParseError("Nenhum arquivo enviado")

        file = request.data['file']

        try:
            chars = random.sample(string.ascii_lowercase + string.digits, 15)
            key = ''.join(map(str, chars)).upper()

            obj_file = HostsFiles.objects.create(key=key, file=file, status='R')
            _id = obj_file.id
            file_path = f"{settings.MEDIA_ROOT}/{obj_file.file.name}".replace('\\', '/')

            if file.name[-3:] == 'csv':
                exception_list = data_csv_tratament(file_path, obj_file)
            else:
                return Response("Formato de arquivo errado!", status=HTTP_406_NOT_ACCEPTABLE)

            if len(exception_list) > 0:
                dataframe = pd.DataFrame(exception_list)
                dataframe.to_csv(f"{settings.MEDIA_ROOT}/files/excecao_{key}.csv".replace("\\", "/"),
                                 sep=',', index=None)
                obj_file.exceptions_file = f"{settings.MEDIA_ROOT}/files/excecao_{key}.csv".replace(
                    "\\", "/")

            obj_file.status = 'F'
            obj_file.save()

            return Response("Importado com sucesso !", status=HTTP_200_OK)

        except Exception as error:
            HostsFiles.objects.filter(id=_id).update(
                status='E', exceptions=error)
            return Response(f"Erro interno: {error}", status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def get_all_files(self, request):
        queryset = HostsFiles.objects.all().order_by('-id')
        serializer = HostsFilesSerializer(queryset, many=True).data

        serializer = [{
            "title": file['file'][13:],
            "date":  datetime(int(file['date'][:4]), int(file['date'][5:7]), int(file['date'][8:10])).strftime('%d/%m/%Y'),
            "status": file['status'],
            "exceptions_file": f"http://192.168.0.47:8000/static/media/excecao_{file['key']}.csv" if
            file['exceptions_file'] is not None else None,
        }
            for file in serializer]

        return Response(serializer, status=HTTP_200_OK)
