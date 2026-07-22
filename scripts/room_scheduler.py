# room_scheduler.py
"""Automated room schedule generation from Revit."""

import sys
import csv
from collections import defaultdict


class RoomScheduleExporter:
    """Extract room data from Revit and export schedules."""
    
    def __init__(self):
        self.rooms = []
    
    def add_room(self, number, name, area, department, occupancy):
        self.rooms.append({
            "number": number, "name": name, "area": area,
            "department": department, "occupancy": occupancy,
        })
    
    def export_csv(self, path="docs/sample_schedule.csv"):
        """Export room schedule to CSV."""
        if not self.rooms:
            print("No rooms to export")
            return
        keys = self.rooms[0].keys()
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.rooms)
        print(f"Exported {len(self.rooms)} rooms to {path}")
    
    def summary(self):
        depts = defaultdict(list)
        for r in self.rooms:
            depts[r["department"]].append(r)
        print("\n=== Room Schedule Summary ===")
        for dept, rooms in sorted(depts.items()):
            total = sum(r["area"] for r in rooms)
            print(f"  {dept}: {len(rooms)} rooms, {total:.1f} m²")


if __name__ == "__main__":
    exporter = RoomScheduleExporter()
    exporter.add_room("A101", "Lecture Hall", 120.5, "Education", 80)
    exporter.add_room("B202", "Design Studio", 85.0, "Architecture", 30)
    exporter.add_room("C303", "Computer Lab", 60.0, "Computing", 25)
    exporter.summary()
    exporter.export_csv()
