# Projet Shiny Living Dex Python
Ce projet utilise Python pour créer une application de Pokedex interactif affichant des images de Pokémon, en mettant l'accent sur les Pokémon shiny. Voici une description détaillée des fichiers inclus et de leur fonctionnement :

# Fichiers inclus :
1. load_data.py
    - Description : Contient des fonctions pour télécharger des données Pokémon depuis une feuille de calcul Google Sheets et préparer les images des Pokémon pour une génération spécifique.
    - Fonctionnalités :
        - Utilisation de pandas pour charger des données Pokémon à partir d'un fichier Excel (SLD.xlsx).
        - Téléchargement et stockage d'images Pokémon shiny à partir de PokémonDB.
        - Gestion dynamique des fichiers d'images : téléchargement des nouvelles images et suppression des anciennes si nécessaire.

2. main.py
    - Description : L'application principale qui utilise Pygame pour afficher le Pokedex interactif à l'écran.
    - Fonctionnalités :
        - Affiche les images des Pokémon pour une génération sélectionnée par l'utilisateur.
        - Calcule et affiche une barre de progression indiquant le pourcentage de Pokémon shiny dans la génération.
        - Capture et sauvegarde l'écran comme une image PNG à chaque sélection de génération.

2. process.py
    - Description : Contient une fonction pour traiter les images des Pokémon avant de les afficher dans Pygame.
    - Fonctionnalités :
        - Utilisation de Pillow (PIL) pour ouvrir et traiter les images.
        - Rotation des images et conversion en niveaux de gris si nécessaire avant l'affichage dans Pygame.
        - Initialisation du projet :
Pour utiliser ce projet, suivez ces étapes d'initialisation :

# Initialisation du projet :
1. Installation des dépendances :
    - Assurez-vous d'installer les packages Python nécessaires en exécutant les commandes suivantes dans votre environnement virtuel ou global :
        - pip install pygame pillow pandas
        - pip install openpyxl
        - pip install gdown

2. Téléchargement des données Pokémon :
    - Utilisez la fonction download_google_sheets dans load_data.py en spécifiant le lien vers votre feuille de calcul Google Sheets pour télécharger les données (SLD.xlsx). Vous pouvez également copier la feuille à partir du lien:
        - https://docs.google.com/spreadsheets/d/14zgiVrEq1io3lgKCHc0gOt9k-d3sb7qxHgN2Ae9BwQc/edit?usp=sharing

3. Exécution de l'application :
    - Lancez main.py pour démarrer l'application. Vous pourrez sélectionner une génération de Pokémon à afficher et observer le Pokedex interactif avec les images des Pokémon correspondants.

# Auteur
Ce projet a été développé par Clément Vongsanga. Pour toute question, suggestion ou contribution, n'hésitez pas à ouvrir une issue ou à proposer une pull request sur GitHub.
