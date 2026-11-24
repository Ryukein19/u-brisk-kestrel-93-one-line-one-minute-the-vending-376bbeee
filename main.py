import os
# One-liner entry (109 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "You must be exact change, because every time you pass, my coil turns and I drop something sweet just for you."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
