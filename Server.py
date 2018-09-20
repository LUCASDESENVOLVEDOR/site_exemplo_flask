from flask import Flask
from flask import render_template

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
    
if __name__ == "__main__":
    App.run(port=80)