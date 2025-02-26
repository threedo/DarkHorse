# DarkHorse
Scripts to retrieve your comics that you downloaded from the DarkHorse reader app and turn those files into PDFs and CBZ files.


DarkHorse Comic Organizer: A Python script to organize and convert Dark Horse digital comics into PDF and CBZ formats.

What does this script do? Scans and processes all comic folders inside the Books directory. Adds a jpg file extension to all the comic pages within each book directory Reads the manifest.json file in each comic folder to determine the correct page order. Renames image files based on their page order. Converts images into a PDF and a CBZ file for easy reading. Generates a UUID mapping CSV file to help rename comics manually.

Author's comments: 

Dark Horse told me (in an email) that soon their app would shut down and all the books I've acquired over the years would be gone (thanks). Their FAQ even goes as far as saying that you can't have them because they are protected. But here's the thing... technically, you already have them and they are sitting on your computer somewhere. This script will grab them, sort them and output them into a PDF and CBZ file.

This process was rather complicated because of how the files are stored, so bare with me as I explain each step, but I promise the end result is a nice organized PDF or CBZ of the comics you collected in your bookshelf (and yes... without any DRM).

The first thing you want to do is download their app (which btw won't be available for much longer. Once downloaded, log in to your account and go to "bookshelf"... which displays all your comics. You will need to click on each one in order to download them to your computer.

On Mac, they are downloaded to the Libray/Containers/Dark Horse/Bookshelf/Books folder and each one uses a UUID as its name. (UUID meaning a bunch of letters and numbers that mean diddly shit to you). Unfortunately, I don't believe there is an app on PC for this. The app only exists for Apple and Android (and who knows how much longer they will keep them live).

READ THIS---------------> Once you found the "Dark Horse" folder... Make a new folder called "DarkHorse" (notice there is no space) and copy the Data/Documents/Bookshelf/Books folder to it.

In each UUID is a bunch of files with no file extensions and two files with JSON extensions. These JSON files are the manifest files. THey contain the order that these files go in. My script will add a jpg file extension to each of these files, then parse the manifest file to put them in the correct order. It will also rename the files with a number so you can easily see the order. Unfortunately, there was no reference to the book name in either manifest so the folders will remain as a UUID name. But don't worry, I added a line in the script to output a CSV file in the Output folder with all the UUID's so you can use a second script Ill write to rename them properly.

The last thing my script will do is output each of these comics (now in order) as a single PDF per folder, and CBZ file for your comic reader program.
Feel free to branch my script and make it better.

Cheers!

-Threedo

-------------------------------------------

Instructions

DarkHorse Comic Organizer – Step-by-Step Guide

*these instructions are specific to Mac because the Dark Horse Digital app is only available in the Apple and Android store.

1. Install Python 3
Before you begin, make sure you have Python 3 installed on your computer. Python 3 is usually pre-installed on Mac, but you can check by typing “python3 –version” in Terminal. If it’s not installed, download and install it from python.org. 

2. Install Required Python Modules
Once Python 3 is installed, you need to install the required dependencies. Open a terminal or command prompt and type “pip install pillow img2pdf”. If “pip” isn’t working, try “python3 -m pip install pillow img2pdf”. This installs the necessary tools to process images and create PDFs.

3. Locate Your Comics Folder
You need to find where Dark Horse saves your downloaded comics. On Mac, comics are stored in “Library/Containers/Dark Horse/Data/Documents/Bookshelf/Books/”. Each comic is inside a folder with a UUID as the name. 

4. Prepare Your Comics for the Script
Because the original “Dark Horse” folder has a space in its name, I had issues running the script. To avoid this problem, create a new folder in the same location as your Books folder and name it “DarkHorse” (without the space). Then, make a folder in that called "Data" and one in that called "Documents" and one in that called "Bookshelf" and one in that called "Books". Then copy the folders in the Books folder over to it. The end result should be a folder called DarkHorse with the same folder structure as the one with a space. Below is a diagram. Hope this helps and is clear.

Library/Containers/Dark Horse (this is the original Dark Horse folder the app creates. Notice it has a space in the name)/Data/Documents/Bookshelf/Books/(Copy these folders)
    
Now go to Library/Containers and make this path: DarkHorse (this is the folder you create. Notice there is NO space)/Data/Documents/Bookshelf/Books/(Paste those folders)

5. Download and Run the Script
In this step, you need to run my script. So either paste it to a text file, download it from Github, clone the repo, etc... whatever you need to do to get that script on your machine and in a place you can run it. I saved mine in my downloads folder, opened terminal, navigated to the downloads folder and typed: “python3 DarkHorse_Comic_Organizer.py”. If you want to enable debug mode, which provides more details, run “python3 DarkHorse_Comic_Organizer.py –debug”.

6. Check Your Output
Once the script runs successfully, it will generate a folder called “Output” in the Containers/DarkHorse/.../.../.../Books folder (the one you created) in step 4. Inside this folder, you’ll find both PDF and CBZ versions of your comics. The script also creates a “uuid_mapping.csv” file, which contains all the UUIDs found in the processed folders. You can manually edit this file to add the correct comic names, and later use a separate script (which I will add) to rename the folders properly.

7. Troubleshooting
If nothing happens after running the script, ensure that you copied the "Data/Documents/Bookshelf/Books" folder structure inside “DarkHorse”. 

8. Want to Improve the Script?
If you’re comfortable with coding, feel free to fork the GitHub repository and make improvements. If you fix the space issue with “Dark Horse,” congratulations, you’re ahead of where I started! If you make useful changes, consider submitting a pull request so others can benefit as well.

Now go read your comics!
