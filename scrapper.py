import requests
from bs4 import BeautifulSoup

# Lanzamos HTTP request
url = "https://stockanalysis.com/list/madrid-stock-exchange/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parseamos el contenido HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extraemos la data de los <td>
td_values = soup.find_all("td")  # Example: extracting all <h2> tags with class "title"

# Step 4: Save data (optional)
with open("output/raw_data.txt", "w") as file:
    for td in td_values:
        file.write(td.text + "\n")