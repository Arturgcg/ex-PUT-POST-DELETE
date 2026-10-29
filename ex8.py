from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
jogos_DB = []

@app.route("/jogos")
def retornarJogos():
    return jsonify(jogos_DB)

@app.route("/jogos", methods=["POST"])
def salvarJogos():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")

    jogo = {"id": id,
    "nome": nome,
    "genero": genero,
    "ano": ano}

    jogos_DB.append(jogo)

    return jsonify(jogo)

@app.route("/jogos/<int:id>", methods=["PUT"])
def editarJogos(id):
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")

    for jogo in jogos_DB:
        if jogo["id"] == id:
            jogo["nome"] = nome
            jogo["genero"] = genero
            jogo["ano"] = ano
            return jsonify(jogo), 200

    return jsonify({"erro": "Jogo não encontrado."}), 404

@app.route("/jogos/<int:id>", methods=["DELETE"])
def removerJogos(id):
    for jogo in jogos_DB:
        if jogo["id"] == id:
            jogos_DB.remove(jogo)
            return "", 204

    return jsonify({"erro": "Jogo não encontrado."}), 404

app.run(debug=True)