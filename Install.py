import os
import sys
try:
    from WindowsContextMenu.menu_operations import *
except ImportError:
    print("You need to install the WindowsContextMenu package.")
    print("git clone https://github.com/offerrall/WindowsContextMenu")
    print("cd WindowsContextMenu")
    print("pip install .")


try:
    python_path = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), "splitsvg.py")

    full_command = f'"{python_path}" "{script_path}" "%1"'

    create_simple_command("EXTENSION_SFA_.svg", "Split SVG", full_command)
except Exception as e:
    print("Need to run as administrator.")