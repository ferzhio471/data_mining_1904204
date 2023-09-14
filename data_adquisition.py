import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

"""
DEFINICION DE FUNCIONES

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_csv_from_url(url:str) -> pd.DataFrame:
    s=requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))"""

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

"""
OBTENER DATAFRAME DESDE URL

df = get_csv_from_url("URL")
print_tabulate(df)
df.to_csv("ruta", index=False)"""

#OBTENER DATAFRAME DESDE ARCHIVO CSV

df = pd.read_csv('C:/Users/ferzh/Desktop/DM/data_mining_1904204/csv/Incidentes_viales_cdmx_limpio.csv', encoding = 'latin1')
print_tabulate(df)#verificar si se obtuvo de manera correcta





