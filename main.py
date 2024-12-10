import os
import shutil
import datetime
from parser import cleanse_data, parse_data_to_dataframe
from scrapper import data_scrapper

# Si la carpeta output ya posee data la mueve a la carpeta de historico
if os.path.exists('output/spain_stocks.csv'):
    date = datetime.date.today()
    shutil.move('output/spain_stocks.csv', f'historic/spain_stocks_{date}.csv')

else: # Si no posee data, se escrapean los datos, se limpian y se incluyen en un archivo csv
    data_scrapper()
    clean_data = cleanse_data()
    df = parse_data_to_dataframe(clean_data)
    df.to_csv("output/spain_stocks.csv")