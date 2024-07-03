import mysql.connector
import pandas as pd 
import matplotlib.pyplot as plt

# Conexión a la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clima',
)


query = 'SELECT dia_del_año, t_minima FROM datos'


df = pd.read_sql(query, connection)


df['dia_del_año'] = df['dia_del_año'].astype(int)

# meses y sus rangos de días
meses = {
    'Enero': (1, 31),
    'Febrero': (32, 59),
    'Marzo': (60, 90),
    'Abril': (91, 120),
    'Mayo': (121, 151),
    'Junio': (152, 181),
    'Julio': (182, 212),
    'Agosto': (213, 243),
    'Septiembre': (244, 273),
    'Octubre': (274, 304),
    'Noviembre': (305, 334),
    'Diciembre': (335, 365)
}

print("Elige un mes para mostrar la temperatura mínima:")
for i, mes in enumerate(meses.keys(), start=1):
    print(f"{i}. {mes}")

eleccion = int(input("Ingresa el número del mes (1-12): "))
mes_elegido = list(meses.keys())[eleccion - 1]
rango_dias = meses[mes_elegido]


mes_df = df[(df['dia_del_año'] >= rango_dias[0]) & (df['dia_del_año'] <= rango_dias[1])]


print(mes_df)


plt.figure(figsize=(12, 6))
plt.bar(mes_df['dia_del_año'] - rango_dias[0] + 1, mes_df['t_minima'], color='b', label='Temperatura mínima')


plt.title(f'Temperatura Mínima del Mes de {mes_elegido}')
plt.xlabel('Día del Mes')
plt.ylabel('Temperatura Mínima (°C)')
plt.xticks(range(1, rango_dias[1] - rango_dias[0] + 2))  # rango de los días del mes 1-12
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

connection.close()

""" tengo una BD llamada roomies, con una tabla llamada roomies, en ella tengo varios datos. Lo que quiero realizar es un poryecto de python en el caual mediante un ainterfaz grafica
    yo pueda colocar el id del candidato y que mediante las impotacions de flask y numpy me dé un grafico en el cual me muestre la compatiblidad que tenga el candidato 
    con el que m´s coincidan los datos  se asimilen más ya que esto me dara una idea de quien podría compartir cuarto con quien."""