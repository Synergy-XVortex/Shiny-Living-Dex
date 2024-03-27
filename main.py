# Import the required libraries
import pygame
from load_data import load_generation_data
from load_data import download_google_sheets
from process import process_image


# Main function
def main():
  pygame.init()  # Initialize Pygame
  pygame.display.set_caption('Shiny Living Dex')  # Set window title
  DISPLAYSURF = pygame.display.set_mode((1920, 1080))  # Create display surface
  Taille = 96  # Image size
  Size = (Taille, Taille)  # Image size tuple
  link = "https://docs.google.com/spreadsheets/d/14zgiVrEq1io3lgKCHc0gOt9k-d3sb7qxHgN2Ae9BwQc/edit?usp=sharing"
  output_path = 'SLD.xlsx'
  download_google_sheets(link, output_path)

  while True:
    # Prompt the user to select a generation to display
    feuille = [
    "Première", "Deuxième", "Troisième", "Quatrième", "Cinquième", "Sixième",
    "Septième", "Huitième", "Neuvième", "Zarbi", "Alola", "de Galar", "Hisui",
    "de Paldea", "Alternatives"
  ]
    for i in range(len(feuille)):
      if i < 9 :
        print(i+1, feuille[i], "Génération")
      if i > 8 :
        print(i+1, "Formes", feuille[i])
    selected_generation = int(
      input("\nEnter the generation number (1-15) or 0 to quit: "))
    if selected_generation == 0:
      pygame.quit()
      quit()

    if selected_generation < 1 or selected_generation > 15:
      print("Invalid generation number.")
      continue

    pokedex, gen = load_generation_data(selected_generation)

    total_pokemon = len(pokedex)
    total_shiny = len(gen)

    x, y = 0, 20  # Reset image coordinates

    images = []  # List to store loaded images and their positions
    for i, pokemon in enumerate(pokedex):
      image_path = f"generation/{selected_generation}/{pokemon}.jpg"  # Path to the image
      if pokemon in gen:
        image = pygame.image.load(image_path).convert()  # Load the image
      else:
        image = process_image(image_path,
                              Taille)  # Process the image for display
      image = pygame.transform.scale(image, Size)  # Scale the image
      images.append((image, (x, y)))  # Store image and position
      x += Taille  # Move to the next column

      if x + Taille > 1920:  # If column is full, move to the next row
        x = 0
        y += Taille

    DISPLAYSURF.fill((0, 0, 0))  # Clear the screen

    # Calculate and display progress bar for shiny Pokémon
    shiny_percentage = (total_shiny / total_pokemon) * 100
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255),
                     (0, 0, shiny_percentage * 19.2, 20))  # White background
    pygame.draw.rect(
      DISPLAYSURF, (0, 255, 0),
      (0, 0, shiny_percentage * 19.2, 20))  # Green shiny progress

    # Display shiny percentage text
    font = pygame.font.Font(None, 36)
    text = font.render(f"Shiny: {shiny_percentage:.2f}%", True,
                       (255, 255, 255))  # Render text
    text_rect = text.get_rect(center=(960, 10))  # Set text position
    DISPLAYSURF.blit(text, text_rect)  # Display text on the screen

    # Display Pokémon images on the screen
    for image, position in images:
      DISPLAYSURF.blit(image, position)

    pygame.display.update()  # Update the display

    # Capture the screen contents
    screen_capture = pygame.Surface(DISPLAYSURF.get_size())
    screen_capture.blit(DISPLAYSURF, (0, 0))

    # Save the screen capture as an image
    pygame.image.save(
      screen_capture,
      f'image/generation_{selected_generation}.png')  # Save as PNG


if __name__ == "__main__":
  main()  # Run the main function when the script is executed
