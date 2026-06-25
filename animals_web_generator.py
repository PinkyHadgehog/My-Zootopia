import json

#1. Funktion definieren
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


# 2. JSON laden
animals_data = load_data("animals_data.json")


# 3. HTML-String erzeugen
def serialize_animal(animal):
    name = animal["name"]
    diet = animal["characteristics"].get("diet", "Unknown")
    animal_type = animal["characteristics"].get("type", "Unknown")
    slogan = animal["characteristics"].get("slogan", "No slogan available")

    if animal["locations"]:
        location = animal["locations"][0]
    else:
        location = "Unknown"

    return f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text">
            <strong>Diet:</strong> {diet}<br/>
            <strong>Location:</strong> {location}<br/>
            <strong>Type:</strong> {animal_type}<br/>
            <strong>Slogan:</strong> {slogan}<br/>
        </p>
    </li>
    """

animals_html = ""

for animal in animals_data:
        animals_html += serialize_animal(animal)


# 4. Template einlesen
with open("animals_template.html", "r") as file:
    html = file.read()


# 5. Platzhalter ersetzen
html = html.replace("__REPLACE_ANIMALS_INFO__", animals_html)


# 6. Neue HTML-Datei schreiben
with open("animals.html", "w") as file:
    file.write(html)