from vulnerabilities.models import Vulnerability
from .models import Host
import pandas as pd
import numpy as np
from datetime import datetime


def get_severity_by_media(media):
    if media == 0.0:
        severity = 'None'
    elif media > 0.1 and media < 3.9:
        severity = 'Baixa'
    elif media > 4.0 and media < 6.9:
        severity = 'Média'
    elif media > 7.0 and media < 8.9:
        severity = 'Alta'
    elif media > 9.0 and media < 10.0:
        severity = 'Crítico'
    else:
        severity = 'None'

    return severity


def create_vulnerabilitie(row):
    try:
        date_pub = row[5].split('/')

        payload = {
            'title': row[2],
            'severity': row[3],
            'cvss': row[4],
            'publication_date': datetime(int(date_pub[2]), int(date_pub[0]), int(date_pub[1])),
            'corrected': False
        }

        vulne = Vulnerability.objects.create(**payload)

        return vulne
    except Exception as error:
        raise error


def create_host(vulne, row):
    try:
        payload = {
            'hostname': row[0],
            'ip_adress': row[1],
        }

        host = Host.objects.create(**payload)
        host.vulnerabilities.add(vulne)
        host.save()
    except Exception as error:
        raise error


def update_host(vulne, host):
    try:
        host.vulnerabilities.add(vulne)
        host.save()

    except Exception as error:
        raise error


def data_csv_tratament(file_path, file):
    exception_list = []
    count = 0
    try:
        readCSV = pd.read_csv(file_path, delimiter=',', skiprows=1, encoding='utf8')
        readCSV = readCSV.replace(np.nan, '', regex=True)

        for index, row in readCSV.iterrows():
            print(row)
            # TODO 0 - ASSET - HOSTNAME | 1 - ASSET - IP_ADDRESS | 2 - VULNERABILITY - TITLE | 3 - VULNERABILITY - SEVERITY | 4 - VULNERABILITY - CVSS | 5 - VULNERABILITY - PUBLICATION_DATE
            if len(row) != 6:
                exception_list.append(
                    f'Linha: {count} | HOST: {row[0]} | IP: {row[1]} - Excecao: Não inserido (Linha esta fora do padrao)')
            else:
                if row[0] is '':
                    exception_list.append(
                        f'Linha: {count} | HOST: {row[0]} | IP: {row[1]} - Excecao: Não inserido (Nome do Host não pode estar vazio)')

                if row[1] is '':
                    exception_list.append(
                        f'Linha: {count} | HOST: {row[0]} | IP: {row[1]} - Excecao: Não inserido (Endereço IP não pode estar vazio)')

                if row[2] is '' or row[3] is '' or row[4] is '':
                    exception_list.append(
                        f'Linha: {count} | HOST: {row[0]} | IP: {row[1]} - Excecao:  Não inserido (Vulnerabilidade deve ser informada por completo)')

                if row[5] is '':
                    exception_list.append(
                        f'Linha: {count} | HOST: {row[0]} | IP: {row[1]} - Excecao:  Não inserido (Data deve ser informada)')

                else:
                    host = Host.objects.filter(hostname=row[0])

                    if host.exists():
                        vulne = create_vulnerabilitie(row)
                        update_host(vulne, host.first())

                    else:
                        vulne = create_vulnerabilitie(row)
                        create_host(vulne, row)
            count += 1

    except Exception as exception:
        exception_list.append(f'Linha: {count} | HOST: {row[0]} | IP: {row[1]} - Excecao: {exception})')
        file.status = 'E'
        file.exception = exception
        file.save()

    return exception_list
