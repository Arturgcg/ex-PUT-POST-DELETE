from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
restaurantes_DB = []

@app.route("/restaurantes")
def retornarRestaurantes():
    return jsonify(restaurantes_DB)

@app.route("/restaurantes", methods=["POST"])
def salvarRestaurantes():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")

    restaurante = {"id": id,
    "nome": nome,
    "tipo": tipo,
    "cidade": cidade}

    restaurantes_DB.append(restaurante)

    return jsonify(restaurante)

@app.route("/restaurantes/<int:id>", methods=["PUT"])
def editarRestaurantes(id):
    dados = request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")

    for restaurante in restaurantes_DB:
        if restaurante["id"] == id:
            restaurante["nome"] = nome
            restaurante["tipo"] = tipo
            restaurante["cidade"] = cidade
            return jsonify(restaurante), 200

    return jsonify({"erro": "Restaurante não encontrado."}), 404

@app.route("/restaurantes/<int:id>", methods=["DELETE"])
def removerRestaurantes(id):
    for restaurante in restaurantes_DB:
        if restaurante["id"] == id:
            restaurantes_DB.remove(restaurante)
            return "", 204

    return jsonify({"erro": "Restaurante não encontrado."}), 404

app.run(debug=True)