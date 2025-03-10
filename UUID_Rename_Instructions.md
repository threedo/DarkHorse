Here are the instructions for getting those ugly UUID comic book names renamed to the actual comic book titles.

<ul>
  <li><span style="color: blue; font-weight: bold;">Step 1: Open a Browser and go to your Bookshelf</span>
    <ul>
      <li>Open a browser and go to <a href="https://digital.darkhorse.com" target="_blank">digital.darkhorse.com</a> and login. I used Google Chrome. At the time of this post, the version is 133.0.6943.142.</li>
      <li>Navigate to your bookshelf.</li>
      <li>On the bookshelf page there is a checkbox called "list comics by series." Make sure this is not checked as we want to see each comic individually. I believe the page can only show up to 25 comics per page, so if you have hundreds of books, there will be many pages.</li>
    </ul>
  </li>
  
  <li><span style="color: blue; font-weight: bold;">Step 2: Using the Browser's Developer Tools</span>
    <ul>
      <li>Open the Developer tools (I believe you can do this by pressing F12, or by opening the "view" menu and selecting Developer/Developer tools).</li>
      <li>Make sure to select the "Console" tab in the developer tools so you can run the code below.</li>
    </ul>
  </li>
  
  <li><span style="color: blue; font-weight: bold;">Step 3: Run the JQuery in your Console</span>
    <ul>
      <li>Run the code below by copying it here, and pasting it in the console and pressing enter.</li>
      <li>This code below is JQuery, compliments of jblaker. Copy it and paste it into the console and press enter:</li>
    </ul>
  </li>

<pre>
var titles = "";

$(".bookshelf-item").each(function() { 
  var uuid=$(this).attr("id");
  var title=$("p.bookshelf-item-title", $(this)).html();
  var pair = uuid + "," + title + "\r";
  titles += pair;
});

console.log(titles);
</pre>

  <li><span style="color: blue; font-weight: bold;">Step 4: Save the Output to a File</span>
    <ul>
      <li>After running this JQuery in the console, it will return the UUIDs and titles of all the comics on the bookshelf page you are on. They will be all jumbled together.</li>
      <li>You will need to copy these details and paste them elsewhere as we will need it later. For example, when I copied the contents, I pasted them into a blank Google Sheet.</li>
    </ul>
  </li>
  
  <li><span style="color: blue; font-weight: bold;">Step 5: Rinse and Repeat</span>
    <ul>
      <li>Once you got it pasted somewhere, go back to the browser and with the developer tools still open, go to the next page in your bookshelf.</li>
      <li>Then run the query again and copy and paste the results again. Keep doing this until you have done it for all the pages you have of comics.</li>
    </ul>
  </li>

  <li><span style="color: blue; font-weight: bold;">Step 6: Clean up the List</span>
    <ul>
      <li>Now go to the list you made, and make sure one column is called "uuid" (with no quotes), and the other is called "title" (with no quotes). Make sure all the UUIDs are in the UUID column and the comic book titles are in the column called title.</li>
      <li>Noteworthy: you can use the Split Text to Columns feature if you need to separate the UUIDs from the Titles.</li>
    </ul>
  </li>

  <li><span style="color: blue; font-weight: bold;">Final Step: Create a CSV and Run the Script</span>
    <ul>
      <li>Save the file as a CSV file to your downloads folder and make sure it is called <code>uuid_mapping.csv</code> (it must be named that for the script to work).</li>
      <li>Run the script titled <code>rename_cbz.py</code> and it will rename all your books that are sitting in the Output folder with a UUID as its title.</li>
    </ul>
  </li>
</ul>
