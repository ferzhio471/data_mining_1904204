import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()
#DATA IMPORTING FROM CSV

df = pd.read_csv('C:/Users/ferzh/Desktop/DM/data_mining_1904204/csv/Incidentes_viales_cdmx_limpio.csv', encoding = 'latin1')

#DATA STATISTICS

#Desviacion estandar: es una medida de la dispersión de los datos, cuanto mayor sea la dispersión mayor
#es la desviación estándar, si no hubiera ninguna variación en los datos, es decir, si fueran todos iguales,
#la desviación estándar sería cero.
print("\n\nDATA STATISTICS\nStandard Deviation\n")
print(df.std())

print("\n\nNon NaN Rows\n")
print(df.count())

print("\n\n")
print(df.describe())

df['fecha_creacion'] = pd.to_datetime(df['fecha_creacion'], format="%d/%m/%Y")
#df.loc[df["hora_creacion"]] = datetime.strptime(df["hora_creacion"], )
df["hora_creacion"]= pd.to_datetime(df['hora_creacion']).dt.time
df['hora_creacion'] = pd.to_datetime(df['hora_creacion'], format="%H:%M:%S")

#df['fecha_creacion', 'hora_creacion'].plot()
#df['fecha_creacion'].plot()

#figsize para tamaño de los ejes x,y
fig, ax= plt.subplots(figsize=(150,50))
#grafica de relacion entre la hora y la fecha del incidente
plt.scatter(df['hora_creacion'], df['fecha_creacion'], alpha=0.5)

#labeling ejes
plt.ylabel("Fecha del incidente vial")
plt.xlabel("Hora del incidente vial")
plt.title("Accidentes viales CDMX 2019")
plt.savefig('C:/Users/ferzh/Desktop/DM/data_mining_1904204/plots/Scatter_incidentes.png')
print("\n\nPLOT 1")

#histograma de las fechas de los incidentes
fechas = df['fecha_creacion']
plt.figure()
plt.hist(fechas)
plt.xlabel("Fecha del incidente vial")
plt.ylabel("Incidente ocurrido")
plt.savefig("C:/Users/ferzh/Desktop/DM/data_mining_1904204/plots/Hist_incidentes.png")
print("\n\nPLOT 2")

#histograma de los meses del incidente vial
fig, ax= plt.subplots(figsize=(50,10))
fechas = df['mes_cierre']
plt.figure()
plt.hist(fechas)
plt.xlabel("Mes del incidente vial")
plt.ylabel("Incidente ocurrido")
plt.savefig("C:/Users/ferzh/Desktop/DM/data_mining_1904204/plots/Hist_mes_incidentes.png")
print("\n\nPLOT 3")



#df.to_csv('C:/Users/ferzh/Desktop/DM/data_mining_1904204/csv/Incidentes_viales_cdmx_limpio.csv', encoding = 'latin1', index=False)
print("\n\nDONE")