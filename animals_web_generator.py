import json

#1. Funktion definieren
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


# 2. JSON laden
animals_data = load_data("animals_data.json")


# 3. HTML-String erzeugen
animals_html = ""

for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"].get("diet", "Unknown")
    animal_type = animal["characteristics"].get("type", "Unknown") #wenn type existiert, verwende ihn, wenn nicht, dann verwende "unknown"
    if animal["locations"]:
        location = animal["locations"][0]
    else:
        location = "Unknown"

    animals_html += f"""
    <li class="cards__item">
        Name: {name}<br/>
        Diet: {diet}<br/>
        Type: {animal_type}<br/>
        Location: {location}<br/>
    </li>
    """

"""
animals_html += "<li class='cards__item'>"
animals_html += f"Name: {name}<br/>"
animals_html += f"Diet: {diet}<br/>"
animals_html += f"Type: {animal_type}<br/>"
animals_html += f"Location: {location}<br/>"
animals_html += "</li>"
"""

# 4. Template einlesen
with open("animals_template.html", "r") as file:
    html = file.read()


# 5. Platzhalter ersetzen
html = html.replace("__REPLACE_ANIMALS_INFO__", animals_html)


# 6. Neue HTML-Datei schreiben
with open("animals.html", "w") as file:
    file.write(html)