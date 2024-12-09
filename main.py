from parser import cleanse_data, parse_data_to_dataframe
from scrapper import data_scrapper

# Se escrapean los datos, se limpian y se anhaden a un archivo csv
data_scrapper()
clean_data = cleanse_data()
df = parse_data_to_dataframe(clean_data)
df.to_csv("output/spain_stocks.csv")