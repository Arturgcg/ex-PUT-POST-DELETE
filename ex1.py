from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
filmes_DB = []

@app.route("filmes")
def retornarFilmes():
    return jsonify(filmes_DB)

@app.route("/filmes", methods=["POST"])
def salvarFilmes():
    global id
    id = id + 1 
    dados =  request.get_json()
    nome = dados.get("nome")
    diretor = dados.get("diretor")
    ano = dados.get("ano")

    filme = {"id": id,
    "nome": nome,
    "diretor": diretor,
    "ano": ano}

    filmes_DB.append(filme)

    return jsonify(filme)

@app.route("/filmes/<int:id>", methods=["PUT"])
def editarFilmes(id):
    dados = request.get_json
    nome = dados.get("nome")
    diretor = dados.get("diretor")
    ano = dados.get("ano")
    for filme in filmes_DB:
        if filme["id"] == id:
            filme["nome"] = nome
            filme["diretor"] = diretor
            filme["ano"] = ano
            return jsonify(filme), 200

    return jsonify ({"erro": "Filme não encontrado."}), 404

@app.route("/filmes/<int:id>", methods=["DELETE"])
def removerFilmes(id):
    for filme in filmes_DB:
        if filme["id"] == id:
            filmes_DB.remove(filme)
            return "", 204

    return jsonify({"erro":"Filme não encontrado"}), 404


app.run(debug=True)