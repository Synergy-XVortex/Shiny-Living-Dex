# Import the required libraries
import pandas as pd
import requests
import gdown
import os


# Function to download and prepare Pokémon data for a specific generation
def load_generation_data(generation_number):
  gen_data = []  # List to store all Pokémon names
  shiny_gen_data = []  # List to store shiny Pokémon names

  # Load data from an Excel spreadsheet
  feuille = [
    "Première", "Deuxième", "Troisième", "Quatrième", "Cinquième", "Sixième",
    "Septième", "Huitième", "Neuvième", "Zarbi", "Alola", "de Galar", "Hisui",
    "de Paldea", "Alternatives"
  ]
  if generation_number <= 9:
    df = pd.read_excel(
      "SLD.xlsx", sheet_name=f"{feuille[generation_number - 1]} Génération")
  if generation_number >= 10:
    df = pd.read_excel("SLD.xlsx",
                       sheet_name=f"Formes {feuille[generation_number - 1]}")

  existing_files = set(os.listdir(f'generation/{generation_number}/'))

  # Liste des fichiers à conserver
  files_to_keep = set()

  # Iterate through the rows of the dataframe
  for index, row in df.iterrows():
    gen_data.append(
      row[df.columns[1]].lower())  # Store Pokémon names in lowercase
    if row[df.columns[3]] == "Oui":
      shiny_gen_data.append(
        row[df.columns[1]].lower())  # Store shiny Pokémon names in lowercase
    a = row[df.columns[2]].lower()
    b = row[df.columns[1]].lower()
    image_path = f'generation/{generation_number}/{b}.jpg'
    files_to_keep.add(
      f'{b}.jpg'
    )  # Ajouter le fichier actuel à la liste des fichiers à conserver

    if b + '.jpg' not in existing_files:
      # Télécharger l'image seulement si elle n'existe pas déjà
      response = requests.get(
        f'https://img.pokemondb.net/sprites/home/shiny/2x/{a}.jpg')
      with open(image_path, 'wb') as f:
        f.write(response.content)

  # Supprimer les fichiers qui ne sont plus nécessaires
  for existing_file in existing_files:
    if existing_file not in files_to_keep:
      file_path = os.path.join(f'generation/{generation_number}/',
                               existing_file)
      # Vérifier si le fichier existe avant de le supprimer
      if os.path.exists(file_path):
        os.remove(file_path)

  return gen_data, shiny_gen_data


def download_google_sheets(link, output_path):
  # Extraire l'ID du lien Google Sheets
  file_id = link.split('/')[-2]

  # Construire l'URL de téléchargement direct
  download_url = f'https://drive.google.com/uc?id={file_id}'

  # Vérifier si le fichier existe déjà, et le supprimer s'il existe
  if os.path.exists(output_path):
    os.remove(output_path)

  # Télécharger le fichier
  gdown.download(download_url, output_path, quiet=False)


# Utilisation de la fonction pour télécharger le fichier
google_sheets_link = 'https://docs.google.com/spreadsheets/d/14zgiVrEq1io3lgKCHc0gOt9k-d3sb7qxHgN2Ae9BwQc/edit?usp=sharing'
output_file_path = 'SLD.xlsx'  # Spécifiez le chemin où vous souhaitez enregistrer le fichier
download_google_sheets(google_sheets_link, output_file_path)
