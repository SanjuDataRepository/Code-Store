# Code-Store
Code Snippets and Documentation for Power BI Projects

Code-Store helps you extract and decode metadata from Power BI project files (.pbip) and Visual Log files from your browser, combining them into a human-readable tabular format. This makes analyzing and understanding Power BI reports faster and much more intuitive.

🚀 Features

- Parse .pbip files to extract visuals, pages, bookmarks, and filters.

- Decode visual types, IDs, and settings into readable formats.

- Read browser Visual Log files to map visual IDs to titles.

- Combine all metadata into a comprehensive tabular report.

- Save time by eliminating tedious manual JSON inspection.

📝 Use Case: 

You are a Power BI developer tasked with building a complex report. The report has:

- Multiple pages for different regions and product categories.

- Several charts and slicers per page.

- Bookmarks for quick navigation between insights.

- Filters applied at visual and page levels.

You carefully place every visual on the report, connect it to the right dataset, configure the filters, and finalize bookmarks. The report looks perfect on your screen.

Days pass by and now you or a teammate need to audit or understand the report behind the scenes. You open the .pbip file and your memory about the report construction is not that fresh.

- The file is a maze of JSON. Every visual has a VisualID but most have generic visual names like slicer or chart.

- You have five slicers on the first page. Which one is the “Region Selector” and which one is the “Product Filter”?

- Bookmarks and filters are buried deep in nested JSON objects. Understanding what each bookmark does is tedious.

You think: “There has to be a better way…”

Then you remember that Power BI Playground logs every visual interaction in your browser. The logs contain human-readable visual titles and page IDs, but they are messy and hard to read directly. Opening the log feels like deciphering an ancient scroll.

This is where Code-Store can help piece everything together:

- It reads the .pbip file and extracts visuals, pages, filters, and bookmarks.

- It reads the browser log file and maps visual IDs to actual visual titles.

- It combines everything into a clean tabular report, so you can instantly see:

    - Which visual belongs to which page

    - What type of visual is it

    - Its filters and settings

    - Associated bookmarks
      
    - Associated tooltips 

And so many more details.

Now, instead of hours of manual JSON digging, you have a single table that tells the whole story of your report.
