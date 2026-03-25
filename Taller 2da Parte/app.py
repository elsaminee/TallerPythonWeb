from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

#Inicializar la base de datos
def init_db():
    conn = sqlite3.connect('tarea.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tarea (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            estado TEXT
        )
    ''')


    
    conn.commit()
    conn.close()

#Obtener conexión a la base de datos
def get_db():
    conn = sqlite3.connect('tarea.db')
    return conn


#Pagina principal
@app.route('/', methods=['GET'])
def inicio():
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT * FROM tarea')
    tareas = c.fetchall()
    conn.close()
    return render_template('index.html', tareas=tareas)


#Agregar tarea
@app.route('/add', methods=['POST'])
def add():
    nombre = request.form['nombre']   # nombre = Tarea1
    estado = request.form['estado']   # estado = Pendiente
    conn = get_db()
    c = conn.cursor()
    c.execute('INSERT INTO tarea (nombre, estado) VALUES (?, ?)', (nombre, estado))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    nombre = request.form['nombre']
    estado = request.form['estado']
    conn = get_db()
    c = conn.cursor()
    c.execute('UPDATE tarea SET nombre = ?, estado = ? WHERE id = ?', (nombre, estado, id))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM tarea WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')



if __name__ == '__main__':
    init_db()
    app.run(debug=True)