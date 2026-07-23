# BIM-Automation

Parametric BIM content & schedule generators for architecture workflows.

> ⚠️ **Status: standalone Python generators (partial).** Produces Revit / Dynamo-ready definitions and schedules as data; live Revit API / Dynamo interop is planned.

## What's implemented

- **`family_generator.py`** — builds parametric **door / window family definitions** (parameters, dimensions, types) and exports them as `family_definitions.json`.
- **`room_scheduler.py`** — compiles a room list and exports a **CSV room schedule** with department area summaries.

## Honest notes

- These are **pure-Python data generators** (stdlib `json` / `csv`). They do **not** currently call the Revit API or run inside Dynamo.
- The generated JSON / CSV are structured to drop into Revit / Dynamo pipelines later.

## Roadmap

- Revit API (`pythonnet` + `RevitAPI.dll`) live family creation.
- Dynamo `.dyn` graph generation from the same definitions.

## Run

```bash
python family_generator.py   # -> family_definitions.json
python room_scheduler.py     # -> room_schedule.csv
```

## Sample outputs (generated)

The generators' output is committed so the repo is self-demonstrating
without a Revit / Dynamo session:

- [`families/family_definitions.json`](families/family_definitions.json) — 3 sample families (2 doors, 1 window)
- [`docs/sample_schedule.csv`](docs/sample_schedule.csv) — 3-room schedule
- [`docs/SAMPLE_OUTPUT.md`](docs/SAMPLE_OUTPUT.md) — rendered preview (tables)

## License

MIT
