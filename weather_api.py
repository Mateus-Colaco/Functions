# extrai_infos
# HTTP ERROR 429 - Limite de requisicoes atingidas
import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

def getWeatherAPI(data_fim: datetime, delta: int, key: str, city: str):
  data_inicio = data_fim + timedelta(days=delta)

  data_inicio = data_inicio.strftime("%Y-%m-%d")
  data_fim = data_fim.strftime("%Y-%m-%d")


  city = 'Bauru'

  URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/', f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')
  file_path = f'home/millenagena/Documents/datapipeline/{data_inicio}/'
  os.mkdir(file_path)
  dados = pd.read_csv(URL)
  dados.to_csv(file_path + 'dados_brutos.csv')
  dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
  dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
