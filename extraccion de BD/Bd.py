import mysql.connector
import pandas as pd 
import matplotlib.pyplot as plt


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='clima',
)

query='select * from datos'

query='SELECT dia_del_año, t_minima FROM  datos'

df=pd.read_sql(query,connection)

print (df.head())

print(df.min())

connection.close()

# Porducto punto/ distancia euclidiana
# Numpy/flask
