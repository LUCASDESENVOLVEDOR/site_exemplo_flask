from flask import Flask
from flask import render_template
import Grupos


App = Flask(__name__, template_folder='./')

@App.route("/", methods=["GET"])
@App.route("/home", methods=["GET"])
def Home():
    return render_template("home.html")

@App.route("/contato", methods=["GET"])
def Contato():
    return render_template("contato.html")

@App.route("/sobre", methods=["GET"])
def Sobre():
    return render_template("sobre.html")

@App.route("/agenda", methods=["GET"])
def Agenda():
    return render_template("/agenda.html")


@App.route("/nome/<Param1>", methods=["GET"])
def nome(Param1):
    Recebido = Param1
    return render_template("nome.html",nome=Recebido)


@App.route("/cadastrar", methods=["GET"])
def cadastrar():
    Grupos.GravaAlunos()
    return render_template("home.html")


@App.route("/alunos",  methods=["GET"])
def alunos():  
    Nomes = Grupos.ListarAlunos()
    return render_template("alunos.html",Nomes=Nomes)


    
if __name__ == "__main__":
    App.run(port=80, debug=True)