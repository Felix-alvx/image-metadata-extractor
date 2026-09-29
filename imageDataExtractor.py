# Extractor de metadata de imágenes

# 1. Instalar Pillow si no está instalado
import sys
import subprocess

try: 
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    print("[!] Pillow no está instalado. Instalando automáticamente...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image
    from PIL.ExifTags import TAGS


# 2. Función para extraer metadatos de imagen
def get_metadata(image_path):
    # Limpiar comillas si el usuario arrastra la imagen a la terminal
    image_path = image_path.replace('"', '').replace("'", "")
    
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        print(f"\n[+] Metadata para: {image_path}")
        print("-" * 45)

        if not exif_data:
            print("[!] No se encontraron metadatos EXIF en la imagen.")
            return

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            # Evitar imprimir bytes crudos muy largos
            if isinstance(value, bytes):
                value = value[:20] + b"..." if len(value) > 20 else value
            print(f"{tag_name:25}: {value}")

    except FileNotFoundError:
        print(f"[-] Error: No se encontró el archivo '{image_path}'.")
    except Exception as e:
        print(f"[-] Ocurrió un error: {e}")


# 3. Función principal para ejecutar el extractor de metadatos
if __name__ == "__main__":
    print("--- IMAGE METADATA EXTRACTOR ---")

    file_path = input("Ingrese la ruta de la imagen: ").strip()
    get_metadata(file_path)

 