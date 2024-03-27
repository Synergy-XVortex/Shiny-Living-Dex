# Import the required libraries
import pygame
from PIL import Image
import numpy as np


# Function to process an image and convert it for display
def process_image(image_path, Taille):
  try:
    img = Image.open(image_path)
  except Image.UnidentifiedImageError:
    # Create a withe square image if there's an error
    img = Image.new("L", (Taille, Taille), color=255)
  else:
    img = img.rotate(90, expand=True)  # Rotate the image
    img = img.convert("L")  # Convert image to grayscale

  img_array = np.array(img)
  img_rgb_array = np.stack((img_array, ) * 3, axis=-1)
  return pygame.surfarray.make_surface(np.uint8(img_rgb_array))
