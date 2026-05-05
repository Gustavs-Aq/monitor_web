from flask import Blueprint, request, jsonify
from services.monitor_service import (
    criar_site,
    listar_sites,
    verificar_site,
    relatorio_site
)

monitor_bp = Blueprint("monitor", __name__)

@monitor_bp.route("/sites", methods=["POST"])
def criar():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"erro": "url obrigatoria"}), 400

    criar_site(url)

    return jsonify({"msg": "site cadastrado"})

@monitor_bp.route("/sites", methods=["GET"])
def listar():
    return jsonify(listar_sites())

@monitor_bp.route("/sites/<int:id>/check", methods=["POST"])
def check(id):
    resultado = verificar_site(id)
    return jsonify(resultado)

@monitor_bp.route("/sites/<int:id>/relatorio")
def relatorio(id):
    return jsonify(relatorio_site(id))