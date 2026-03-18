from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/saludo')
def saludo():
    return render_template('saludo.html')

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        return f"Hola, {nombre}!"
    return render_template("formulario.html")   


if __name__ == '__main__':
    app.run(debug=True)
