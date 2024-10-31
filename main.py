import argparse
from PIL import Image
import os

# Configura las dimensiones para las versiones redimensionadas (en píxeles)
sizes = {
    "thumbnail": (150, 150),     # Tamaño para thumbnails
    "medium": (800, 800),        # Tamaño para vistas previas
    "large": (1200, 1200)        # Tamaño más grande para otras utilidades
}

# Configuración de argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Redimensiona imágenes en una carpeta específica.")
parser.add_argument("--path", type=str, required=True, help="Ruta de la carpeta de imágenes.")
args = parser.parse_args()

input_folder = args.path

# Procesa cada imagen en la carpeta
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Carga la imagen original
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Guarda la imagen redimensionada para cada tamaño especificado
            for size_name, dimensions in sizes.items():
                # Redimensiona la imagen
                resized_img = img.copy()
                resized_img.thumbnail(dimensions)
                
                # Guarda la imagen redimensionada en la misma carpeta de entrada
                base, ext = os.path.splitext(filename)
                output_path = os.path.join(input_folder, f"{base}_{size_name}{ext}")
                resized_img.save(output_path)
                print(f"Imagen guardada en {output_path}")
