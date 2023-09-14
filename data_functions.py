import pandas as pd

"""
OBTENER DATAFRAME DESDE URL

df = get_csv_from_url("URL")
print_tabulate(df)
df.to_csv("ruta", index=False)"""

#DATA IMPORTING FROM CSV

df = pd.read_csv('C:/Users/ferzh/Desktop/DM/data_mining_1904204/csv/incidentes-viales-2019.csv', encoding = 'utf-8')


#DATA CLEANING

#Funciones ya no necesarias debido a encoding utf8 en entrada y latin1 en salida

#df.rename(columns={'aÃ±o_cierre': 'year_cierre'}, inplace=True)
#df.loc[df["dia_semana"] == "MiÃ©rcoles", "dia_semana"] = "Miercoles"
#df.loc[df["dia_semana"] == "SÃ¡bado", "dia_semana"] = "Sabado"

#Elimina las filas donde todos los elementos son null
df.dropna(how='all', inplace=True)

#Organiza de manera ascendente y agrupando por ciertas columnas
df.sort_values(by=['fecha_creacion', 'hora_creacion'], ascending=True, inplace=True)


df.to_csv('C:/Users/ferzh/Desktop/DM/data_mining_1904204/csv/Incidentes_viales_cdmx_limpio.csv', encoding = 'latin1', index=False)
print("DONE")



