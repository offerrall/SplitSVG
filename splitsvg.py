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

    # Find all groups and paths within groups
    groups = root.findall('.//svg:g', ns)

    for i, group in enumerate(groups):
        # Create a new 'svg' element with the same attributes as the original
        new_svg = ET.Element('svg', xmlns="http://www.w3.org/2000/svg", version="1.1")
        
        # Set important attributes for correct display
        new_svg.set('width', svg_width)
        new_svg.set('height', svg_height)
        if svg_viewbox:
            new_svg.set('viewBox', svg_viewbox)

        # Copy the group of paths to the new SVG
        new_group = ET.SubElement(new_svg, 'g', attrib=group.attrib)
        
        for path in group.findall('.//svg:path', ns):
            path_copy = ET.Element('path', attrib=path.attrib)
            path_copy.text = path.text
            new_group.append(path_copy)
        
        # Create a new element tree and save the SVG file
        new_tree = ET.ElementTree(new_svg)
        output_file = os.path.join(output_dir, f"group_{i + 1}.svg")
        new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
        
        print(f"Exported {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extracts all groups and paths from an SVG file and saves them as separate SVG files.")
    parser.add_argument("svg_file", help="Path to the input SVG file.")
    
    args = parser.parse_args()
    
    if not exists(args.svg_file):
        print("The file does not exist.")
    elif not args.svg_file.endswith(".svg"):
        print("The file is not an SVG.")
    else:
        extract_paths_from_svg(args.svg_file)
