# Zootopia Animals Website

Zootopia Animals Website is a Python project that generates an HTML website displaying information about animals. The project fetches data from the API Ninjas Animals API
 and displays it as styled cards.

The problem it solves: instead of manually looking up animal details, users can enter an animal name and instantly get its type, diet, and location displayed in a neat, visually appealing HTML page.

Intended audience: anyone interested in learning about animals or practicing Python, APIs, and HTML generation.
## Features

- Fetch animal data from the API by name
- Display animal info as styled cards in HTML
- Handles non-existing animals gracefully with a friendly message
- Uses `.env` file to securely store the API key

## Installation:

1. Clone the repository:
git clone <your-repo-url>
cd zootopia-api

## Install dependencies:

pip install -r requirements.txt

# Usage
python animals_web_generator.py

- Enter the name of an animal when prompted.

- The program will generate animals.html with the animal cards.

- If the animal doesn’t exist, a friendly message will be displayed.
