from flask import Flask, render_template, request, jsonify
import mysql.connector
import os

# Caminhos corretos
base_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.abspath(os.path.join(base_dir, '..', '..', 'app', 'static'))
template_folder = os.path.join(base_dir, 'templates')

# Flask app
app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)

# Conexão com MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestao_alunos"
)

@app.route('/')
def home():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    try:
        dados = request.json
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome_aluno, idade_aluno, email, curso_id) VALUES (%s, %s, %s, %s)",
            (dados['nome'], dados['idade'], dados['email'], dados['curso_id'])
        )
        db.commit()
        return jsonify({"mensagem": "Aluno cadastrado!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
