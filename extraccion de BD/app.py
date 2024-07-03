from flask import Flask, request, render_template
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Conectar a la base de datos MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='roomies',
    )
    return connection

# Ruta principal para ingresar el nombre
@app.route('/')
def index():
    connection = get_db_connection()
    query = 'SELECT nombre FROM roomies'
    df = pd.read_sql(query, connection)
    connection.close()
    nombres = df['nombre'].tolist()
    return render_template('index.html', nombres=nombres)

# Ruta para procesar la búsqueda de roomies
@app.route('/find_roomies', methods=['POST'])
def find_roomies():
    name = request.form['name']
    connection = get_db_connection()
    query = 'SELECT * FROM roomies'
    df = pd.read_sql(query, connection)
    connection.close()

    # Filtrar el usuario por nombre
    user = df[df['nombre'] == name]
    if user.empty:
        return 'No se encontró a la persona con ese nombre.'

    user_data = user.iloc[0]
    df = df[df['nombre'] != name]  # Eliminar al usuario de la lista de posibles roomies

    # Calcular compatibilidad (esto es un ejemplo simple, puedes ajustarlo según tus necesidades)
    compatibility_scores = []
    for idx, row in df.iterrows():
        score = np.sum(user_data == row) / len(df.columns)
        compatibility_scores.append(score)

    df['compatibility'] = compatibility_scores
    df_sorted = df.sort_values(by='compatibility', ascending=False)

    # Graficar compatibilidad
    plt.figure(figsize=(12, 6))
    plt.bar(df_sorted['nombre'], df_sorted['compatibility'], color='b')
    plt.xlabel('Nombre')
    plt.ylabel('Compatibilidad')
    plt.title('Compatibilidad con ' + name)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar la gráfica
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.savefig('static/compatibility.png')
    plt.close()

    return render_template('result.html', name=name, roomies=df_sorted[['nombre', 'compatibility']].head(5))

if __name__ == '__main__':
    app.run(debug=True)
