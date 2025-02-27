import os
import json
import csv
import shutil
import glob
import img2pdf
from zipfile import ZipFile

# Detect user home directory
HOME_DIR = os.path.expanduser("~")
CONTAINERS_DIR = os.path.join(HOME_DIR, "Library", "Containers")

# Function to find the correct Dark Horse UUID dynamically
def find_dark_horse_uuid():
    for container_path in glob.glob(os.path.join(CONTAINERS_DIR, "*")):
        uuid = os.path.basename(container_path)  # Get the folder name (UUID or "Dark Horse")

        # Check if it's a valid UUID format (36 characters, including dashes)
        if len(uuid) == 36 and uuid.count('-') == 4:
            bookshelf_path = os.path.join(container_path, "Data/Documents/Bookshelf")
            if os.path.isdir(bookshelf_path):  # Confirm the Bookshelf folder exists
                return uuid  # Return the UUID

    return None  # Return None if not found

# Get the correct UUID dynamically
dark_horse_uuid = find_dark_horse_uuid()

# If found, construct the Books directory path
if dark_horse_uuid:
    BASE_DIR = os.path.join(CONTAINERS_DIR, dark_horse_uuid, "Data/Documents/Bookshelf/Books")
    print(f"✅ Dark Horse UUID found: {dark_horse_uuid}")
    print(f"📂 Books directory: {BASE_DIR}")
else:
    print("❌ Dark Horse container not found!")
    exit()

# Define output directory
OUTPUT_DIR = os.path.join(HOME_DIR, "Desktop", "Output")
UUID_MAPPING_FILE = os.path.join(OUTPUT_DIR, "uuid_mapping.csv")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Get list of comic folders (UUIDs)
comic_folders = [f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f)) and len(f) == 32]

if not comic_folders:
    print("❌ No comic folders found. Exiting.")
    exit()

# Initialize UUID mapping
uuid_mapping = []

for comic_uuid in comic_folders:
    comic_path = os.path.join(BASE_DIR, comic_uuid)
    manifest_path = os.path.join(comic_path, "manifest.json")

    if not os.path.exists(manifest_path):
        print(f"  ❌ Skipping {comic_uuid}: No manifest.json found")
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
            if os.path.exists(old_path) and not old_path.endswith(".jpg"):
                new_jpg_path = old_path + ".jpg"
                os.rename(old_path, new_jpg_path)
                old_path = new_jpg_path  # Update reference to renamed file

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
        print(f"✅ Processed {comic_uuid}")

# Write UUID mapping file
with open(UUID_MAPPING_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["UUID", "Comic Name"])
    writer.writerows(uuid_mapping)

print("\n🎉 ✅ All comics processed! Check the 'Output' folder on your Desktop.")
