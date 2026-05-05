from repository.monitor_repository import (
    insert_site,
    get_sites,
    get_site_by_id,
    insert_check,
    get_checks_by_site
)
import requests
import datetime
import time

def criar_site(url):
    insert_site(url)

def listar_sites():
    return get_sites()

def verificar_site(site_id):
    site = get_site_by_id(site_id)

    if not site:
        return {"erro": "site nao encontrado"}

    url = site["url"]

    inicio = time.time()

    try:
        response = requests.get(url)
        status = response.status_code
    except:
        status = 0

    fim = time.time()
    tempo = fim - inicio

    data = str(datetime.datetime.now())

    insert_check(site_id, status, tempo, data)

    return {
        "url": url,
        "status": status,
        "tempo": round(tempo, 3)
    }

def relatorio_site(site_id):
    checks = get_checks_by_site(site_id)

    total = len(checks)

    media = 0
    if total > 0:
        soma = 0
        for c in checks:
            soma += c["tempo"]
        media = soma / total

    return {
        "total_checks": total,
        "tempo_medio": round(media, 3),
        "historico": checks
    }