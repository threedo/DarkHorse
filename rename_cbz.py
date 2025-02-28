import os
import csv

# Paths
OUTPUT_DIR = os.path.expanduser("~/Desktop/Output")  # Adjust if needed
MAPPING_FILE = os.path.expanduser("~/Downloads/uuid_mapping.csv")  # Adjust to where you saved it

# Load UUID → Title mapping from CSV
uuid_to_title = {}
with open(MAPPING_FILE, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        if len(row) == 2:
            uuid_to_title[row[0]] = row[1]

# Rename CBZ files
for filename in os.listdir(OUTPUT_DIR):
    if filename.endswith(".cbz"):
        uuid = filename.replace(".cbz", "")  # Get UUID from filename
        if uuid in uuid_to_title:
            new_filename = f"{uuid_to_title[uuid]}.cbz"
            old_path = os.path.join(OUTPUT_DIR, filename)
            new_path = os.path.join(OUTPUT_DIR, new_filename)

            # Rename file
            os.rename(old_path, new_path)
            print(f"✅ Renamed {filename} → {new_filename}")

print("✅ All CBZ files renamed successfully!")
