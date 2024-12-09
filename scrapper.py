import requests
from bs4 import BeautifulSoup

def data_scrapper(url: str = "https://stockanalysis.com/list/madrid-stock-exchange/", key_element: str = "td"):

    '''Dada una URL y un elemento clave (elemento de HTML, <td>, <div>, etx) extrae tomos los valores de la pagina que 
    esten almacenados dentro de ese elemento clave y los almacena en el file "raw_data.txt", dentro de la carpeta output.''' 

    # Lanzamos HTTP request
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # Parseamos el contenido HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Extraemos la data que este almacenada en el elemento clave
    element_values = soup.find_all(key_element)

    # Guardamos la data extraida
    with open("output/raw_data.txt", "w") as file:
        for element in element_values:
            file.write(element.text + "\n")