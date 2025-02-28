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
            uuid_to_title[row[0].strip()] = row[1].strip()  # Strip spaces

# Rename CBZ and PDF files
for filename in os.listdir(OUTPUT_DIR):
    file_path = os.path.join(OUTPUT_DIR, filename)

    # Skip directories
    if not os.path.isfile(file_path):
        continue

    # Check if it's a CBZ or PDF file
    if filename.endswith(".cbz") or filename.endswith(".pdf"):
        uuid = filename.replace(".cbz", "").replace(".pdf", "").strip()  # Extract UUID

        if uuid in uuid_to_title:
            # Create new filename
            new_filename = f"{uuid_to_title[uuid]}{os.path.splitext(filename)[1]}"  # Keep original extension
            new_path = os.path.join(OUTPUT_DIR, new_filename)

            # Rename file
            try:
                os.rename(file_path, new_path)
                print(f"✅ Renamed {filename} → {new_filename}")
            except Exception as e:
                print(f"❌ Error renaming {filename}: {e}")

print("\n🎉 ✅ All CBZ and PDF files renamed successfully!")
