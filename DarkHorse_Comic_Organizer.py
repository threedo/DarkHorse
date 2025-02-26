import os
import json
import csv
import shutil
import img2pdf
from zipfile import ZipFile

# Detect user home directory
HOME_DIR = os.path.expanduser("~")

# Define base directory dynamically
if os.name == "nt":  # Windows
    BASE_DIR = os.path.join(HOME_DIR, "AppData", "Local", "DarkHorse", "Data", "Documents", "Bookshelf", "Books")
else:  # Mac/Linux
    BASE_DIR = os.path.join(HOME_DIR, "Library", "Containers", "DarkHorse", "Data", "Documents", "Bookshelf", "Books")

# Define output directory
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
UUID_MAPPING_FILE = os.path.join(OUTPUT_DIR, "uuid_mapping.csv")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get list of comic folders (UUIDs)
comic_folders = [f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f)) and len(f) == 32]

if not comic_folders:
    print("No comic folders found. Exiting.")
    exit()

# Initialize UUID mapping
uuid_mapping = []

for comic_uuid in comic_folders:
    comic_path = os.path.join(BASE_DIR, comic_uuid)
    manifest_path = os.path.join(comic_path, "manifest.json")

    if not os.path.exists(manifest_path):
        print(f"Skipping {comic_uuid}: No manifest.json found")
        continue

    # Read manifest file
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # Extract images and sort them in order
    page_data = sorted(manifest.get("pages", []), key=lambda x: x.get("sort_order", 9999))

    image_mapping = []
    for idx, page in enumerate(page_data, start=1):
        src_image = page.get("src_image")
        if src_image:
            old_path = os.path.join(comic_path, src_image)

            # Ensure file has .jpg extension
            if not old_path.endswith(".jpg") and os.path.exists(old_path):
                new_jpg_path = old_path + ".jpg"
                os.rename(old_path, new_jpg_path)
                old_path = new_jpg_path

            new_name = f"{idx:03}.jpg"
            new_path = os.path.join(comic_path, new_name)

            if os.path.exists(old_path):  # Rename to ordered format
                os.rename(old_path, new_path)
                image_mapping.append(new_path)

    # Generate PDF
    if image_mapping:
        pdf_path = os.path.join(OUTPUT_DIR, f"{comic_uuid}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_mapping))

        # Generate CBZ
        cbz_path = os.path.join(OUTPUT_DIR, f"{comic_uuid}.cbz")
        with ZipFile(cbz_path, 'w') as cbz:
            for img in image_mapping:
                cbz.write(img, os.path.basename(img))

        # Append to UUID mapping file
        uuid_mapping.append([comic_uuid, ""])
        print(f"Processed {comic_uuid}")

# Write UUID mapping file
with open(UUID_MAPPING_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["UUID", "Comic Name"])
    writer.writerows(uuid_mapping)

print("✅ All comics processed! Check the Output folder.")
