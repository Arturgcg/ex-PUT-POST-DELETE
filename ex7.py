from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
cidades_DB = []

@app.route("/cidades")
def retornarCidades():
    return jsonify(cidades_DB)

@app.route("/cidades", methods=["POST"])
def salvarCidades():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    cidade = {"id": id,
    "nome": nome,
    "preco": preco,
    "categoria": categoria}

    cidades_DB.append(cidade)

    return jsonify(cidade)

@app.route("/cidades/<int:id>", methods=["PUT"])
def editarCidades(id):
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    for cidade in cidades_DB:
        if cidade["id"] == id:
            cidade["nome"] = nome
            cidade["preco"] = preco
            cidade["categoria"] = categoria
            return jsonify(cidade), 200

    return jsonify({"erro": "Cidade não encontrada."}), 404

@app.route("/cidades/<int:id>", methods=["DELETE"])
def removerCidades(id):
    for cidade in cidades_DB:
        if cidade["id"] == id:
            cidades_DB.remove(cidade)
            return "", 204

    return jsonify({"erro": "Cidade não encontrada."}), 404

app.run(debug=True)