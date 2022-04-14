from flask_app import app

# Imports all the methods our app will use
from flask import render_template, redirect, request

# Sample on how we get class from our models
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

# Routing

# Main Page
@app.route("/dojos")
def main():
    dojos = Dojo.get_all_rows();
    return render_template("dojos.html", dojos=dojos)

# Main Page Dojo Form
@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.insert_row(data)
    return redirect("/dojos")

# Dojo Page that Lists all the ninjas to a dojo
@app.route("/dojos/<int:id>")
def ninjas_dojos(id):
    ninjas = Ninja.get_all_rows_from_dojo(id);
    return render_template("dojo_ninjas.html", ninjas=ninjas)

# New Ninja page that allows the user to create a new ninja
@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all_rows()
    return render_template("ninjas.html", dojos=dojos)

# Route that process the new ninja form and puts it into the database
@app.route("/new_ninja", methods = ["POST"])
def new_ninja():
    print(request.form)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.insert_row(data)
    return redirect("/dojos")