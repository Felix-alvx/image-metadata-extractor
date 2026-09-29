<div align="center">

# 📸 Image Metadata Extractor

**A lightweight, dependency-light CLI tool to extract EXIF metadata from images using Python and Pillow.**

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Code style: PEP8](https://img.shields.io/badge/code%20style-PEP8-brightgreen.svg)](https://peps.python.org/pep-0008/)

</div>

---

## 📑 Table of Contents

- [🇬🇧 English](#-english)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example Output](#example-output)
  - [Project Structure](#project-structure)
  - [Supported Formats](#supported-formats)
  - [What Can EXIF Reveal?](#what-can-exif-reveal)
  - [Legal & Ethical Use](#legal--ethical-use)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
- [🇪🇸 Español](#-español)
  - [Descripción](#descripción)
  - [Características](#características)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Ejemplo de salida](#ejemplo-de-salida)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Formatos soportados](#formatos-soportados)
  - [¿Qué puede revelar el EXIF?](#qué-puede-revelar-el-exif)
  - [Uso legal y ético](#uso-legal-y-ético)
  - [Hoja de ruta](#hoja-de-ruta)
  - [Contribuciones](#contribuciones)
  - [Licencia](#licencia)

---

# 🇬🇧 English

## Overview

**Image Metadata Extractor** is a command-line utility that reads and displays the **EXIF** (Exchangeable Image File Format) metadata embedded in image files.

Photos taken with smartphones, DSLRs and action cameras store a surprising amount of hidden information: exact GPS coordinates, camera serial numbers, precise timestamps, device models and sometimes even software names or geotagged user comments. This tool surfaces that data in a clean, readable format — which is useful for:

- **Digital forensics & OSINT** — verifying whether an image has been tampered with, or locating the source of a leaked photo.
- **Privacy auditing** — checking what your own photos leak before posting them online.
- **Security research** — understanding how metadata can be used in reconnaissance pipelines.

The whole tool fits in a single file and has **one dependency**: [Pillow](https://python-pillow.org/).

> **Educational project.** Intended for authorized security research, personal privacy audits and forensic analysis of media you own or have permission to examine.

## Features

| | Feature |
|---|---|
| 🧩 | **Single-file, zero-config** — one script, no framework, no config files |
| 📦 | **Auto-installs Pillow** — no `pip install` step required on first run |
| 🖼️ | **Wide format support** — anything Pillow can open (JPEG, PNG, TIFF, WebP, ...) |
| 🏷️ | **Human-readable tags** — EXIF tag IDs are resolved to their proper names |
| ✂️ | **Drag & drop friendly** — stray quotes from terminal drag-and-drop are stripped automatically |
| 🛡️ | **Safe error handling** — clear messages for missing files, invalid images and corrupted EXIF blocks |
| 🧹 | **Truncated binary output** — long raw `bytes` values (e.g. `MakerNote`) are trimmed so output stays readable |
| 🎯 | **OSINT-oriented** — clean, parseable text output, easy to pipe into `grep`, `awk` or other tooling |

## Requirements

- **Python 3.7+** (developed and tested on **Python 3.12.10**)
- **Pillow 9.0+** (developed and tested on **Pillow 12.3.0**)
- Any image file containing an EXIF block

Pillow is installed automatically on first run, so a manual install is optional.

## Installation

**Clone the repository:**

```bash
git clone https://github.com/Felix-alvx/image-metadata-extractor.git
cd image-metadata-extractor
```

**Install the dependency manually (recommended for reproducibility):**

```bash
pip install Pillow
```

Using a virtual environment is the cleanest approach:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

pip install Pillow
```

## Usage

Run the script and enter the path to the image you want to analyse:

```bash
python imageDataExtractor.py
```

```
--- IMAGE METADATA EXTRACTOR ---
Ingrese la ruta de la imagen: assets/sample.jpg
```

You can also pass the path directly (e.g. via drag-and-drop in the terminal, or from a script):

```bash
python imageDataExtractor.py "photos/vacation.jpg"
```

**Tips**

- On Windows you can simply **drag the image file onto the terminal window** to paste its full path. Any surrounding quotes are removed automatically.
- Use **quoted paths** if the filename contains spaces: `"C:\Users\me\My Photos\pic.jpg"`.

## Example Output

Running the tool against a Canon compact camera JPEG:

```text
--- IMAGE METADATA EXTRACTOR ---
Ingrese la ruta de la imagen: samples/11-tests.jpg
[+] Metadata para: samples/11-tests.jpg
---------------------------------------------
RelatedImageWidth        : 2272
RelatedImageLength       : 1704
WhiteBalance             : 0
ExposureMode             : 0
CustomRendered           : 0
DigitalZoomRatio         : 1.0
SceneCaptureType         : 0
ExifOffset               : 214
Make                     : Canon
Model                    : Canon DIGITAL IXUS 40
DateTime                 : 2007:09:03 16:03:45
YCbCrPositioning         : 1
ExifVersion              : b'0220'
ComponentsConfiguration   : b'\x01\x02\x03\x00'
CompressedBitsPerPixel   : 3.0
DateTimeOriginal         : 2007:09:03 16:03:45
DateTimeDigitized        : 2007:09:03 16:03:45
ShutterSpeedValue        : 8.96875
ApertureValue            : 2.96875
ExposureBiasValue        : 0.0
MaxApertureValue         : 2.96875
MeteringMode             : 5
Flash                    : 24
FocalLength              : 5.8
UserComment              : b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00...'
ColorSpace               : 1
ExifImageWidth           : 2272
FocalPlaneXResolution    : 10142.857142857143
ExifImageHeight          : 1704
FocalPlaneYResolution    : 10142.857142857143
FocalPlaneResolutionUnit : 2
SensingMethod            : 2
FileSource               : b'\x03'
ExposureTime             : 0.002
FNumber                  : 2.8
FlashPixVersion          : b'0100'
MakerNote                : b'\x11\x00\x01\x00\x03\x00.\x00\x00\x00x\x03\x00\x00\x02\x00\x03\x00\x04\x00...'
```

If the image contains no EXIF block:

```text
[!] No se encontraron metadatos EXIF en la imagen.
```

## Project Structure

```text
image-metadata-extractor/
├── imageDataExtractor.py   # Main script — CLI entry point and EXIF extraction logic
├── README.md               # Project documentation (this file)
├── LICENSE                 # MIT License
├── requirements.txt        # Python dependencies
├── .gitignore              # Python / IDE exclusions
└── samples/                # Sample images for testing
    └── 11-tests.jpg
```

## Supported Formats

Support comes from Pillow, so any format it can open will work. **EXIF data is most commonly present in:**

- **JPEG / JPG**
- **TIFF / TIF**
- **PNG** (eXIf chunk)
- **WebP** (EXIF chunk)
- **HEIC / HEIF** *(requires Pillow with HEIF support)*

> **Note:** PNG and WebP only carry EXIF if it was explicitly written into the file. Most images in these formats are stripped of metadata during export.

## What Can EXIF Reveal?

EXIF blocks frequently contain the following — some of it highly sensitive:

| Category | Typical tags |
|---|---|
| 📍 **Location** | `GPSLatitude`, `GPSLongitude`, `GPSAltitude`, `GPSTimestamp` |
| 🕒 **Timestamps** | `DateTimeOriginal`, `DateTimeDigitized`, `CreateDate`, `ModifyDate` |
| 📷 **Device** | `Make`, `Model`, `SerialNumber`, `LensModel`, `BodySerialNumber` |
| 🎞 **Capture settings** | `FNumber`, `ExposureTime`, `ISO`, `FocalLength`, `Flash`, `WhiteBalance` |
| 🧑 **Identity** | `Artist`, `Copyright`, `OwnerName`, `Software`, `HostComputer`, `UserComment` |
| 📝 **Raw text** | `ImageDescription`, `XPTitle`, `XPSubject`, `XPTags`, `XPDocument` |

> ⚠️ Some social platforms (Instagram, Twitter/X, Facebook) strip most EXIF on upload, but many others — and direct file sharing, email attachments and cloud storage links — do not.

## Legal & Ethical Use

This project is provided for **educational and defensive security purposes only**.

- ✅ Analyse images you **own**
- ✅ Audit your **own** photos before publishing them
- ✅ Work on files you have **explicit written permission** to examine
- ✅ Use it as part of a **CTF** or authorised penetration test

- ❌ Do **not** use it to track, surveil or identify people without their consent
- ❌ Do **not** use extracted personal data for stalking, doxxing or harassment
- ❌ Do **not** use it in violation of local or international privacy laws (e.g. GDPR, CCPA, LOPD/GARR)

**You are solely responsible for how you use this tool.** The authors accept no liability for any misuse.

## Roadmap

- [ ] **Batch mode** — process an entire directory in one run
- [ ] **JSON / CSV output** via `--format` flag for easy piping into other tools
- [ ] **GPS coordinates** formatted as decimal + Google Maps link
- [ ] **Recursive EXIF parsing** (IPTC, XMP, ICC profile) beyond the base block
- [ ] **Metadata sanitiser** mode to strip fields from your own images
- [ ] **Timeline builder** — sort a set of images by capture date
- [ ] **Command-line argument parsing** with `argparse` instead of interactive `input()`
- [ ] **Unit tests** + CI pipeline
- [ ] **Colourised / formatted terminal output**

## Contributing

Contributions are welcome and appreciated.

1. **Fork** the repository
2. **Create a branch** for your feature: `git checkout -b feature/new-parser`
3. **Commit** your changes with a clear message
4. **Push** to your fork and open a **Pull Request**

Please keep the code **PEP 8 compliant**, add **docstrings** to new functions, and document new behaviour in this README.

## License

Released under the **MIT License**. See [`LICENSE`](LICENSE) for the full text.

```text
MIT License

Copyright (c) 2026 Félix Alvarado

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

# 🇪🇸 Español

## Descripción

**Image Metadata Extractor** es una herramienta de línea de comandos que lee y muestra los metadatos **EXIF** (*Exchangeable Image File Format*) incrustados en archivos de imagen.

Las fotos tomadas con smartphones, cámaras réflex y cámaras de acción guardan una cantidad sorprendente de información oculta: coordenadas GPS exactas, números de serie, marcas de tiempo precisas, modelos de dispositivo e incluso nombres de software o comentarios con geolocalización. Esta herramienta muestra esos datos de forma limpia y legible, lo que resulta útil para:

- **Forense digital y OSINT** — verificar si una imagen fue manipulada o localizar el origen de una foto filtrada.
- **Auditoría de privacidad** — comprobar qué filtran tus propias fotos antes de publicarlas en línea.
- **Investigación de seguridad** — entender cómo se pueden usar los metadatos en procesos de reconocimiento.

Toda la herramienta cabe en un solo archivo y tiene **una única dependencia**: [Pillow](https://python-pillow.org/).

> **Proyecto educativo.** Destinado a investigación de seguridad autorizada, auditorías de privacidad personal y análisis forense de archivos propios o sobre los que se tenga permiso.

## Características

| | Característica |
|---|---|
| 🧩 | **Un solo archivo, sin configuración** — un script, sin framework, sin archivos de config |
| 📦 | **Instala Pillow automáticamente** — no hace falta `pip install` en la primera ejecución |
| 🖼️ | **Amplio soporte de formatos** — todo lo que Pillow pueda abrir (JPEG, PNG, TIFF, WebP, ...) |
| 🏷️ | **Etiquetas legibles** — los IDs de tags EXIF se traducen a sus nombres reales |
| ✂️ | **Compatible con arrastrar y soltar** — las comillas sobrantes se eliminan automáticamente |
| 🛡️ | **Manejo seguro de errores** — mensajes claros para archivos inexistentes, imágenes inválidas o EXIF corrupto |
| 🧹 | **Salida binaria truncada** — los valores `bytes` largos (p. ej. `MakerNote`) se recortan para mantener la salida legible |
| 🎯 | **Orientado a OSINT** — salida de texto limpia y fácil de procesar con `grep`, `awk` u otras herramientas |

## Requisitos

- **Python 3.7+** (desarrollado y probado con **Python 3.12.10**)
- **Pillow 9.0+** (desarrollado y probado con **Pillow 12.3.0**)
- Cualquier archivo de imagen que contenga un bloque EXIF

Pillow se instala automáticamente en la primera ejecución, por lo que la instalación manual es opcional.

## Instalación

**Clonar el repositorio:**

```bash
git clone https://github.com/Felix-alvx/image-metadata-extractor.git
cd image-metadata-extractor
```

**Instalar la dependencia manualmente (recomendado para reproducibilidad):**

```bash
pip install Pillow
```

Usar un entorno virtual es la opción más limpia:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

pip install Pillow
```

## Uso

Ejecuta el script e introduce la ruta de la imagen que quieres analizar:

```bash
python imageDataExtractor.py
```

```
--- IMAGE METADATA EXTRACTOR ---
Ingrese la ruta de la imagen: assets/ejemplo.jpg
```

También puedes pasar la ruta directamente (por ejemplo, arrastrando el archivo a la terminal o desde otro script):

```bash
python imageDataExtractor.py "fotos/vacaciones.jpg"
```

**Consejos**

- En Windows puedes **arrastrar el archivo de imagen sobre la ventana de la terminal** para pegar su ruta completa. Las comillas sobrantes se eliminan automáticamente.
- Usa **rutas entre comillas** si el nombre del archivo contiene espacios: `"C:\Users\yo\Mis Fotos\foto.jpg"`.

## Ejemplo de salida

Ejecutando la herramienta sobre un JPEG de una cámara compacta Canon:

```text
--- IMAGE METADATA EXTRACTOR ---
Ingrese la ruta de la imagen: samples/11-tests.jpg
[+] Metadata para: samples/11-tests.jpg
---------------------------------------------
Make                     : Canon
Model                    : Canon DIGITAL IXUS 40
DateTimeOriginal         : 2007:09:03 16:03:45
FNumber                  : 2.8
ExposureTime             : 0.002
FocalLength              : 5.8
Flash                    : 24
ColorSpace               : 1
ExifImageWidth           : 2272
ExifImageHeight          : 1704
MakerNote                : b'\x11\x00\x01\x00\x03\x00.\x00\x00\x00x\x03\x00\x00\x02\x00\x03\x00\x04\x00...'
```

*(Salida completa disponible en la sección [Example Output](#example-output).)*

Si la imagen no contiene datos EXIF:

```text
[!] No se encontraron metadatos EXIF en la imagen.
```

## Estructura del proyecto

```text
image-metadata-extractor/
├── imageDataExtractor.py   # Script principal — punto de entrada CLI y lógica de extracción EXIF
├── README.md               # Documentación del proyecto (este archivo)
├── LICENSE                 # Licencia MIT
├── requirements.txt        # Dependencias de Python
├── .gitignore              # Exclusiones de Python / IDE
└── samples/                # Imágenes de ejemplo para pruebas
    └── 11-tests.jpg
```

## Formatos soportados

El soporte proviene de Pillow, así que funcionará cualquier formato que este pueda abrir. **Los datos EXIF están presentes principalmente en:**

- **JPEG / JPG**
- **TIFF / TIF**
- **PNG** (chunk `eXIf`)
- **WebP** (chunk EXIF)
- **HEIC / HEIF** *(requiere Pillow con soporte HEIF)*

> **Nota:** PNG y WebP solo llevan EXIF si se escribió explícitamente en el archivo. La mayoría de las imágenes en estos formatos se limpian de metadatos al exportarlas.

## ¿Qué puede revelar el EXIF?

Los bloques EXIF suelen contener lo siguiente, y parte de ello es altamente sensible:

| Categoría | Etiquetas típicas |
|---|---|
| 📍 **Ubicación** | `GPSLatitude`, `GPSLongitude`, `GPSAltitude`, `GPSTimestamp` |
| 🕒 **Marcas de tiempo** | `DateTimeOriginal`, `DateTimeDigitized`, `CreateDate`, `ModifyDate` |
| 📷 **Dispositivo** | `Make`, `Model`, `SerialNumber`, `LensModel`, `BodySerialNumber` |
| 🎞 **Ajustes de captura** | `FNumber`, `ExposureTime`, `ISO`, `FocalLength`, `Flash`, `WhiteBalance` |
| 🧑 **Identidad** | `Artist`, `Copyright`, `OwnerName`, `Software`, `HostComputer`, `UserComment` |
| 📝 **Texto libre** | `ImageDescription`, `XPTitle`, `XPSubject`, `XPTags`, `XPDocument` |

> ⚠️ Algunas plataformas sociales (Instagram, Twitter/X, Facebook) eliminan la mayoría del EXIF al subir, pero muchas otras —y el compartir archivos directamente, adjuntos de correo y enlaces de almacenamiento en la nube— no lo hacen.

## Uso legal y ético

Este proyecto se ofrece **únicamente con fines educativos y de seguridad defensiva**.

- ✅ Analizar imágenes que **te pertenezcan**
- ✅ Auditar **tus propias** fotos antes de publicarlas
- ✅ Trabajar sobre archivos para los que tengas **permiso explícito por escrito**
- ✅ Usarlo como parte de un **CTF** o de un test de penetración autorizado

- ❌ No lo uses para rastrear, vigilar o identificar personas sin su consentimiento
- ❌ No uses los datos personales extraídos para acoso, doxxing o acoso
- ❌ No lo uses vulnerando leyes de privacidad locales o internacionales (GDPR, CCPA, LOPD/GARR)

**Eres el único responsable del uso que le des a esta herramienta.** Los autores no asumen ninguna responsabilidad por un uso indebido.

## Hoja de ruta

- [ ] **Modo por lotes** — procesar un directorio entero en una sola ejecución
- [ ] **Salida JSON / CSV** mediante la opción `--format` para integrarlo con otras herramientas
- [ ] **Coordenadas GPS** en formato decimal y enlace a Google Maps
- [ ] **Parseo recursivo de EXIF** (IPTC, XMP, perfil ICC) más allá del bloque base
- [ ] **Modo saneador** para eliminar campos de tus propias imágenes
- [ ] **Constructor de línea de tiempo** — ordenar un conjunto de imágenes por fecha de captura
- [ ] **Parsing de argumentos de línea de comandos** con `argparse` en lugar de `input()` interactivo
- [ ] **Pruebas unitarias** + pipeline de CI
- [ ] **Salida de terminal con colores y mejor formato**

## Contribuciones

Las contribuciones son bienvenidas y apreciadas.

1. Haz **fork** del repositorio
2. **Crea una rama** para tu funcionalidad: `git checkout -b feature/nuevo-parser`
3. **Haz commit** de tus cambios con un mensaje claro
4. **Sube** la rama a tu fork y abre un **Pull Request**

Mantén el código **compatible con PEP 8**, añade **docstrings** a las funciones nuevas y documenta los nuevos comportamientos en este README.

## Licencia

Distribuido bajo la **Licencia MIT**. Consulta [`LICENSE`](LICENSE) para el texto completo.

---

<div align="center">

*Remember: metadata is a fingerprint. Strip it before you share.*

</div>
