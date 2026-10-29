from flask import Flask, request, jsonify

app = Flask(__name__)

id = 0
alunos_DB = []

@app.route("alunos")
def retornarAlunos():
    return jsonify(alunos_DB)

@app.route("/alunos", methods=["POST"])
def salvarAlunos():
    global id
    id = id + 1 
    dados =  request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")

    aluno = {"id": id,
    "nome": nome,
    "curso": curso,
    "idade": idade}

    alunos_DB.append(aluno)

    return jsonify(aluno)

@app.route("/alunos/<int:id>", methods=["PUT"])
def editarAlunos(id):
    dados = request.get_json
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    for aluno in alunos_DB:
        if aluno["id"] == id:
            aluno["nome"] = nome
            aluno["diretor"] = curso
            aluno["ano"] = idade
            return jsonify(aluno), 200

    return jsonify ({"erro": "Aluno não encontrado."}), 404

@app.route("/Alunos/<int:id>", methods=["DELETE"])
def removerAlunos(id):
    for aluno in alunos_DB:
        if aluno["id"] == id:
            alunos_DB.remove(aluno)
            return "", 204

    return jsonify({"erro":"Aluno não encontrado"}), 404


app.run(debug=True)