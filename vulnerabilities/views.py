from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from django.core.paginator import Paginator
from .models import Vulnerability
from hosts.models import Host
from .serializers import VulnerabilitiesSerializer


# Register your viewsets here.
class VulnerabilitiesViewSet(viewsets.ModelViewSet):

    @action(methods=['GET'], detail=False)
    def list_vulnerabilities(self, request):
        try:
            page = request.query_params.get('page')
            queryset = Vulnerability.objects.all().distinct('title')

            if not queryset.exists():
                return Response("Nenhuma vulnerabilidade encontrada", status=HTTP_200_OK)

            serializer = VulnerabilitiesSerializer(queryset, many=True).data

            for vulne in serializer:
                hosts = Host.objects.filter(vulnerabilities__title=vulne['title']).count()
                vulne['total_hosts'] = str(hosts)

            hosts = Paginator(serializer, 50)
            page_vulne = hosts.page(page)

            list_vulne= []
            for host in page_vulne.object_list:
                list_vulne.append(host)

            return Response({"listaVulnerabilidades": list_vulne}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar Vulnerabilidades', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def filter_vulnerabilities(self, request):
        try:
            page = request.query_params.get('page')
            host = request.query_params.get('host')
            severity = request.query_params.get('severity')

            if host is not None and host is not '':
                vulne_ids = Host.objects.filter(hostname__istartswith=host).values('vulnerabilities__id')

                if not vulne_ids.exists():
                    return Response("Nenhuma vulnerabilidade encontrada", status=HTTP_200_OK)

                list_vulne_ids = []
                for vulne in vulne_ids:
                    list_vulne_ids.append(vulne['vulnerabilities__id'])

                vulnes_obj = Vulnerability.objects.filter(id__in=list_vulne_ids).distinct('title')
                serializer = VulnerabilitiesSerializer(vulnes_obj, many=True).data

                list_vulnerabilities = []

                if len(serializer) > 0:
                    vulnes = Paginator(serializer, 50)
                    page_vulnes = vulnes.page(page)

                    for vulne in page_vulnes.object_list:
                        list_vulnerabilities.append(vulne)

                return Response({'listVulnerabilities': list_vulnerabilities}, status=HTTP_200_OK)
            else:
                vulne = Vulnerability.objects.filter(severity__istartswith=severity).order_by('cvss')

                if not vulne.exists():
                    return Response("Nenhuma vulnerabilidade encontrada", status=HTTP_200_OK)

                serializer = VulnerabilitiesSerializer(vulne, many=True).data
                list_vulnerabilities = []

                if len(serializer) > 0:
                    hosts = Paginator(serializer, 50)
                    page_vulne = hosts.page(page)

                    for vulne in page_vulne.object_list:
                        list_vulnerabilities.append(vulne)

                return Response({'listaVulnerabilidades': list_vulnerabilities}, status=HTTP_200_OK)

        except Exception as error:
            return Response('Nenhuma lista encontrada', status=HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def correct_vulnerabilitie(self, request):
        try:
            vulne_id = request.data['id']

            if vulne_id is not None or vulne_id is not 'undefined':
                vulne = Vulnerability.objects.filter(id=vulne_id)
                if vulne.exists():
                    vulne.update(corrected=True)
                    return Response('Vulnerabilidade corrigida', status=HTTP_200_OK)
                else:
                    return Response('Vulnerabilidade não corrigida', status=HTTP_200_OK)
            else:
                return Response('ID da vulnerabilidade não informado', status=HTTP_200_OK)

        except Exception as error:
            return Response('Vulnerabilidade não corrigida', status=HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], detail=False)
    def get_total_vulnerabilities(self, request):
        try:
            total = Vulnerability.objects.all().count()
            not_corrected = Vulnerability.objects.filter(corrected=False).count()
            return Response({"totalVulnerabilities": total, "notCorrected": not_corrected}, status=HTTP_200_OK)
        except Exception as error:
            return Response('Error ao carregar Hosts', status=HTTP_500_INTERNAL_SERVER_ERROR)



