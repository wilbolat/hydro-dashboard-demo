#!/usr/bin/env python3
"""
Generate mock Solinst-style CSV files once a minute.
File name format: LS123456_YYYYMMDDHHMM.csv
Row format: YYYY/MM/DD HH:MM, depth(m), temp(C), batt(V)
"""
import csv, time, random, datetime as dt, pathlib, os
OUT_DIR = pathlib.Path(__file__).parent.parent / "mock_data"
OUT_DIR.mkdir(exist_ok=True)
depth = 100.000   # starting elevation in metres
while True:
    ts = dt.datetime.utcnow().replace(second=0, microsecond=0)
    depth += random.gauss(0, 20.002)        # random walk ±2 mm
    temp  = 15 + random.gauss(0, 0.1)      # °C
    batt  = 4.10 - random.uniform(0, 0.0002)
    fname = f"LS123456_{ts.strftime('%Y%m%d%H%M')}.csv"
    fpath = OUT_DIR / fname
    with fpath.open("w", newline="") as f:
        csv.writer(f).writerow(
            [ts.strftime("%Y/%m/%d %H:%M"),
             f"{depth:.3f}", f"{temp:.1f}", f"{batt:.2f}"]
        )
    print("wrote", fpath.relative_to(OUT_DIR.parent))
    time.sleep(60)     # wait one minute

#| **3-D Save the file** | Press **Ctrl + S** (or File → Save). | VS Code shows “●” removed from the tab title. |
#| **3-E Run it once** | In the **terminal** at bottom:<br>`python scripts/mock_level_generator.py` | Every 60 s you’ll see `wrote mock_data/LS123456_...csv`.  Let it run for 2–3 files, then press **Ctrl +C** to stop. |
#| **3-F Peek at a file** | Expand the **`mock_data`** folder in Explorer and click one `.csv` file. | It should contain a single line like:<br>`2025/06/21 12:00, 100.002, 14.9, 4.08` |
#| **3-G Commit your work** | 1. Click the **Source Control** icon (left bar).<br>2. You’ll see the new folders/files listed.<br>3. In the message box type **`Add mock data generator`**.<br>4. Click the **✓ Commit** icon, then “**Sync Changes**”. | Status bar bottom-left returns to `main`, and GitHub now has your script. |






#### Ready for **Step 4** (spinning up InfluxDB + Grafana with Docker Compose and ingesting those CSVs), or any questions on the mock-data script before we continue?
