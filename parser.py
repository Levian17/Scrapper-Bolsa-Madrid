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
    for x in range(0, len(raw_data)-6, 6):
        clean_data.append([raw_data[x], raw_data[x+1], raw_data[x+2], raw_data[x+3], raw_data[x+4], raw_data[x+5]])

    return clean_data