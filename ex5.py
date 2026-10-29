from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
produtos_DB = []

@app.route("/Produtos")
def retornarProdutos():
    return jsonify(produtos_DB)

@app.route("/Produtos", methods=["POST"])
def salvarProdutos():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    produto = {"id": id,
    "nome": nome,
    "preco": preco,
    "categoria": categoria}

    produtos_DB.append(produto)

    return jsonify(produto)

@app.route("/Produtos/<int:id>", methods=["PUT"])
def editarProdutos(id):
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    for produto in produtos_DB:
        if produto["id"] == id:
            produto["nome"] = nome
            produto["preco"] = preco
            produto["categoria"] = categoria
            return jsonify(produto), 200

    return jsonify({"erro": "Produto não encontrado."}), 404

@app.route("/Produtos/<int:id>", methods=["DELETE"])
def removerProdutos(id):
    for produto in produtos_DB:
        if produto["id"] == id:
            produtos_DB.remove(produto)
            return "", 204

    return jsonify({"erro": "Produto não encontrado."}), 404

app.run(debug=True)