# SVG Path Extractor

Este es un sencillo script en Python que permite extraer todos los elementos `<path>` de un archivo SVG y guardarlos como archivos SVG separados. Es útil cuando necesitas desglosar un archivo SVG en sus componentes individuales para un procesamiento posterior.

## Características

- **Sin dependencias externas**: El script utiliza solo módulos estándar de Python (`os`, `xml.etree.ElementTree`, `argparse`).
- **Automatización**: Crea automáticamente un directorio para los archivos SVG exportados.
- **Simplicidad**: El uso es sencillo y directo, solo requiere la ruta al archivo SVG como argumento.

## Requisitos

Este script está escrito en Python y no requiere ninguna dependencia externa. Funciona con cualquier instalación estándar de Python 3.x.

## Instalación

1. Clona este repositorio o descarga el archivo `extract_paths.py`.
2. Asegúrate de tener Python 3.x instalado en tu sistema.

## Uso

Para utilizar el script, abre una terminal y ejecuta el siguiente comando:

```bash
python extract_paths.py /ruta/al/archivo.svg
