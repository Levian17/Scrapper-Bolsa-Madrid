import pandas as pd

def cleanse_data(path_raw_data: str = "output/raw_data.txt") -> list[list[str]]:

    '''Dado el path al archivo que contiene la raw_data, la funcion recorrera el texto limpiando lso "\n" y los "-",
    finalmente agrupa los bloques de informacion dentro de una lista de listas.'''

    raw_data = []
    with open(path_raw_data, "r") as file:
        for line in file.readlines():
            raw_data.append(line)

    for x in range(len(raw_data)):
        if '\n' in raw_data[x]:
            raw_data[x] = raw_data[x].replace("\n", "")
        if raw_data[x] == '-':
            raw_data[x] = None

    clean_data = []
    for x in range(0, len(raw_data)-7, 7):
        clean_data.append([raw_data[x], raw_data[x+1], raw_data[x+2], raw_data[x+3], raw_data[x+4], raw_data[x+5]])

    return clean_data

def parse_data_to_dataframe(clean_data: list[list[str]]) -> pd.DataFrame:
    '''Toma la data que debe haber sido limpiada previamente y la transforma en un Dataframe de pandas.'''

    data_dict = {
        "Abreviatura": [],
        "Nombre Empresa": [],
        "Valor Total": [],
        "Precio Stock": [],
        "Delta Valor": [],
    }

    for stock in clean_data:
        data_dict["Abreviatura"].append(stock[1])
        data_dict["Nombre Empresa"].append(stock[2])
        data_dict["Valor Total"].append(stock[3])
        data_dict["Precio Stock"].append(stock[4])
        data_dict["Delta Valor"].append(stock[5])

    df = pd.DataFrame(data_dict)
    return df