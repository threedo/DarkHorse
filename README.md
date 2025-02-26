DarkHorse Comic Organizer
A Python script to retrieve your downloaded Dark Horse digital comics and convert them into PDF and CBZ files for easy reading.

What This Script Does:
	•	Scans and processes all comic folders inside the Books directory.
	•	Adds missing .jpg file extensions to all comic pages.
	•	Reads the manifest.json file in each comic folder to determine the correct page order.
	•	Renames image files numerically based on page order.
	•	Converts images into a PDF and a CBZ file.
	•	Generates a UUID mapping CSV file to help rename comics manually.

Why I Made This:
Dark Horse announced that their app would soon shut down, and all purchased digital comics would be unavailable. Their FAQ even claimed that users couldn’t access their comics because they were “protected.” However, if you’ve downloaded your comics using their app, they are already on your computer.

This script:
	•	Finds your downloaded comics
	•	Sorts the files
	•	Outputs organized PDF and CBZ files

The process was tricky because the comics are hidden in folders with random UUIDs instead of actual names. But don’t worry—this script helps get them organized.

How to Use This Script

Step 1: Install Python 3
Make sure Python 3 is installed on your computer.
Check by opening Terminal and typing:

python3 –version

If it’s not installed, download it from python.org.

Step 2: Install Required Dependencies
Run the following command in Terminal to install the necessary Python modules:

pip install pillow img2pdf

If you get an error, try:

python3 -m pip install pillow img2pdf

Step 3: Locate Your Comics Folder
On Mac, Dark Horse saves downloaded comics here:

~/Library/Containers/Dark Horse/Data/Documents/Bookshelf/Books/

Each comic is stored in a folder with a UUID name (a long string of letters and numbers).

Important: The original folder name “Dark Horse” has a space in it, which may cause issues when running the script.

Step 4: Copy Comics to a New Folder
To avoid script errors, create a new folder called DarkHorse (without a space).
Then copy your comics from the original folder into this new location.

Folder structure before:
~/Library/Containers/Dark Horse/Data/Documents/Bookshelf/Books/

Folder structure after copying:
~/Library/Containers/DarkHorse/Data/Documents/Bookshelf/Books/

Now your comics are in a space-free directory.

Step 5: Run the Script
	1.	Download the script from GitHub and save it to a folder you can access easily.
	2.	Open Terminal and navigate to where the script is saved.
Example: If saved in Downloads, type:
cd ~/Downloads
	3.	Run the script:
python3 DarkHorse_Comic_Organizer.py
	4.	If you want debug mode (more detailed logs), run:
python3 DarkHorse_Comic_Organizer.py –debug

Step 6: Check Your Output
Once the script runs, check the Output folder:

~/Library/Containers/DarkHorse/Data/Documents/Bookshelf/Books/Output/

Inside this folder, you’ll find:
	•	PDF versions of your comics
	•	CBZ files for comic readers
	•	A uuid_mapping.csv file – this helps manually rename comics later.

Step 7: Troubleshooting
If nothing happens after running the script:
	•	Make sure you copied your comics to DarkHorse (no space).
	•	Ensure Python 3 and dependencies are installed.
	•	Try running the script with –debug for more details.

Step 8: Rename Comics (Optional)
Since UUID folder names are random, the script generates a UUID mapping CSV file (uuid_mapping.csv). You can:
	1.	Manually update this file with real comic names.
	2.	Use a separate script (coming soon) to rename the folders automatically.

Want to Contribute?
Feel free to fork the GitHub repository and improve the script.
	•	Fix bugs
	•	Add Windows support
	•	Make it even better

If you manage to remove the space issue with “Dark Horse,” let me know—you’re a wizard.

Final Thoughts
Dark Horse wanted to lock away your comics forever—but this script lets you keep what you paid for. Now you can read them anytime, DRM-free.

Enjoy!
— Threedo
