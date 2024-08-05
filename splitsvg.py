import os
import xml.etree.ElementTree as ET
from os.path import exists
import argparse

def extract_paths_from_svg(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    ns = {'svg': 'http://www.w3.org/2000/svg'}

    output_dir = os.path.join(os.path.dirname(svg_file), "exported_paths")
    os.makedirs(output_dir, exist_ok=True)

    svg_attribs = root.attrib
    svg_width = svg_attribs.get('width', '100%')
    svg_height = svg_attribs.get('height', '100%')
    svg_viewbox = svg_attribs.get('viewBox')

    paths = root.findall('.//svg:path', ns)

    for i, path in enumerate(paths):
        new_svg = ET.Element('svg', xmlns="http://www.w3.org/2000/svg", version="1.1")
        
        new_svg.set('width', svg_width)
        new_svg.set('height', svg_height)
        if svg_viewbox:
            new_svg.set('viewBox', svg_viewbox)
        
        new_svg.append(path)
        new_tree = ET.ElementTree(new_svg)
        
        output_file = os.path.join(output_dir, f"path_{i + 1}.svg")
        new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
        
        print(f"Exported {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrae todos los paths de un archivo SVG y los guarda como archivos SVG separados.")
    parser.add_argument("svg_file", help="Ruta del archivo SVG de entrada.")
    
    args = parser.parse_args()
    
    if not exists(args.svg_file):
        print("El archivo no existe.")
    elif not args.svg_file.endswith(".svg"):
        print("El archivo no es un SVG.")
    else:
        extract_paths_from_svg(args.svg_file)