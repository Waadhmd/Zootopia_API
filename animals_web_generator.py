from data_fetcher import fetch_data

TEMPLATE_FILENAME = 'animals_template.html'
OUTPUT_HTML_FILENAME = "animals.html"


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
    while True:
        animal_name = input("Enter a name of an animal: ").strip()
        if not animal_name:
            print("Please enter a non-empty animal name")
            continue
        break

    animal_data = fetch_data(animal_name)
    if animal_data:
        animal_info_text = render_animals_text(animal_data)
        print("Website was successfully generated to the file animals.html")
    else:
        animal_info_text = f'''
        <li class="cards__item">
            <div class="card__title">Oops!</div>
            <div class="card__text">
                <p style="color:red; font-weight:bold;">
                    The animal "{animal_name}" doesn't exist.
                </p>
            </div>
        </li>
        '''
        print('problem loading data !')


    html_template = load_html_template(TEMPLATE_FILENAME)
    rendered_html = html_template.replace('__REPLACE_ANIMALS_INFO__', animal_info_text)
    with open(OUTPUT_HTML_FILENAME, 'w') as output_file:
        output_file.write(rendered_html)




if __name__ == '__main__':
    main()
