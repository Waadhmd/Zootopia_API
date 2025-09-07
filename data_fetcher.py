import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "LBEzQVe/r1WOiPVe36JF6Q==GJJKAb0NuU0NBxOJ"

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  headers = {'X-Api-Key': API_KEY}
  response = requests.get(f"{API_URL}?name={animal_name}", headers=headers)
  if response.status_code == 200:
      return response.json()
  else:
      print(f"Error: status {response.status_code}")
      return None