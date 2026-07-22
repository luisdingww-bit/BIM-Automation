# family_generator.py
"""Parametric Revit family generator."""

import json
import math


class FamilyGenerator:
    """Generate Revit families from parametric definitions."""
    
    def __init__(self):
        self.families = []
    
    def create_door_family(self, name, width, height, panel_type):
        """Define a parametric door family."""
        family = {
            "type": "Door",
            "name": name,
            "parameters": {
                "Width": width,
                "Height": height,
                "PanelType": panel_type,
                "Thickness": 0.04,
                "FrameDepth": 0.08,
            }
        }
        self.families.append(family)
        return family
    
    def create_window_family(self, name, width, height, sill_height):
        """Define a parametric window family."""
        family = {
            "type": "Window",
            "name": name,
            "parameters": {
                "Width": width,
                "Height": height,
                "SillHeight": sill_height,
                "FrameDepth": 0.06,
            }
        }
        self.families.append(family)
        return family
    
    def export_json(self, path="families/family_definitions.json"):
        with open(path, "w") as f:
            json.dump(self.families, f, indent=2)
        print(f"Exported {len(self.families)} families to {path}")


if __name__ == "__main__":
    gen = FamilyGenerator()
    gen.create_door_family("D-901", 0.9, 2.1, "Solid Wood")
    gen.create_door_family("D-121", 1.2, 2.1, "Glass")
    gen.create_window_family("W-151", 1.5, 1.5, 0.9)
    gen.export_json()
