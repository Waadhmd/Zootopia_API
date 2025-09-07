import json
import requests

ANIMALS_DATA_FILENAME = 'animals_data.json'
TEMPLATE_FILENAME = 'animals_template.html'
OUTPUT_HTML_FILENAME = "animals.html"
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "LBEzQVe/r1WOiPVe36JF6Q==GJJKAb0NuU0NBxOJ"

def load_data(file_path):
    """
     Load JSON data from a file.
    Returns:
        list: Parsed JSON data as a list of dictionaries
    """
    with open(file_path , 'r') as handle:
        return json.load(handle)

def fetch_animal_data(animal_name):
    """  Fetch animal data from the API Ninjas Animals API by animal name"""
    headers = {'X-Api-Key':API_KEY}
    response = requests.get(f"{API_URL}?name={animal_name}",headers=headers)
    return response.json()


def load_html_template(file_path):
    """
     Load an HTML template file.
    """
    with open(file_path, 'r',encoding="utf-8") as template_file:
        return template_file.read()

def serialize_animal(animal:dict):
    """
    Convert a single animal dictionary into an HTML <li> element
    styled as a card with its details.
    """
    output = ""

    output += '<li class="cards__item">'

    if 'name' in animal:
        output += f"<div class='card__title' > {animal['name']} </div>"
    output += '<div class="card__text">'
    output += '<ul class="cards">'
    diet = animal.get('characteristics', {}).get('diet')

    if diet:
        output += f"<li class='card__detail'><strong>Diet:</strong> {diet} </li>"

    if 'locations' in animal:
        output += f"<li class='card__detail'><strong>Location:</strong> {animal['locations'][0]} </li>"
    animal_type_value = animal.get('characteristics', {}).get('type')

    if animal_type_value:
        output += f"<li class='card__detail'><strong>Type:</strong> {animal_type_value} </li>"
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output

def render_animals_text(animals:list):
    """
    Convert a list of animal dictionaries into a single HTML string
    """
    output = ''
    for animal in animals:
        output += serialize_animal(animal)
    return output

def main():
    """
    - Loads animal data from JSON
    - Converts data into HTML card list
    - Inserts card list into the HTML template
    - Saves the rendered HTML file
    """
    animals = load_data(ANIMALS_DATA_FILENAME)
    animal_info_text = render_animals_text(animals)
    html_template = load_html_template(TEMPLATE_FILENAME)
    rendered_html = html_template.replace('__REPLACE_ANIMALS_INFO__',animal_info_text)

    with open(OUTPUT_HTML_FILENAME , 'w') as output_file:
        output_file.write(rendered_html)

if __name__ == '__main__':
    main()
