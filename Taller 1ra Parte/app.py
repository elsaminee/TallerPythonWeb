from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '¡Hola, mundo!'

@app.route('/saludo')
def saludo():
    return '¡Bienvenido a mi servidor Flask!'

if __name__ == '__main__':
    app.run(debug=True)
