Once you have your comics in the "output" folder, go to digital.darkhorse.com and login. Go to your bookshelf. 

On the bookshelf page there is a checkbox called "list comics by series".. make sure this is not checked as we want to see each comic individually. I believe the page can only show up to 25 comics per page, so if you have hundreds of books, there will be many pages.

Now open the browser's developer tools. I used the latest version of the Google Chrome browser for reference. At the time of this post, the version is 133.0.6943.142.

Now open the Developer tools (I believe you can do this by pressing F12, or by openeing the "view" menu and selecting Developer/Developer tools. 

Now make sure to select the "Console" tab in the developer tools so you can run the code below. 

This code below is JQuery, compliments of jblaker. Copy it and paste it into the console and press enter:

```
var titles = "";

$(".bookshelf-item").each(function() { 
  var uuid=$(this).attr("id");
  var title=$("p.bookshelf-item-title", $(this)).html();
  var pair = uuid + "," + title + "\r";
  titles += pair;
});

console.log(titles);

```

It will return the UUIDs and titles of all the comics on the bookshelf page you are on. 

You will need to copy this and paste it elsewhere as we will need it later. I copied and pasted it into a blank Google Sheet.

Once you got it pasted somewhere, go back to the browser and with the developer tools still open, go to the next page in your bookshelf. 

Then run the query again and copy and paste the results again. Keep doing this until you have done it for all the pages you have of comics. You should now have a very large list of your comic book titles and their assocated UUIDs

Now go to the list you made, and make sure one column is called "uuid" (with no quotes), and the other is called "title" (with no quotes). Make sure all the UUIDs are in the UUID column and the comic book titles are in the column called title.
Noteworthy- you can use the Split Text to Columns feature if you need to separate the UUIDs from the Titles.

Now save the file as a CSV file to your downloads folder and make sure it is called uuid_mapping.csv (it must be named that for the script to work).

Now run the script titled rename_cbz.py and it will rename all your books that are sitting in the Output folder with a UUID as its title.

-Threedo
