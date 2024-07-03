import pandas as pd
from sqlalchemy import create_engine

host='localhost'
usuario='root'
password=''
base_de_datos='accidentes'

conec=create_engine(f'mysql+mysqlconnector://{usuario}:{password}@{host}/{base_de_datos}')

valor_ref_area='ISL'
valor_time_period='2023-Q1'
consulta=f"select * from analisis WHERE area='{valor_ref_area}' AND periodo='{valor_time_period}'"

datos_filtrados=pd.read_sql_query(consulta, conec)

print(datos_filtrados.head())

#necesito que apareza una ves o solo un a serie del area ISl, en la que por los diferentes periodos de tiempo muestre las muertes que hibieron en eos periodos  