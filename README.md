# web-scraping-challenge
Name
Web Scraping Homework 

Description
This project required building a web application that scrapes various websites for data related to the Mission to Mars. The selected text, images and tables are displayed on an HTML page. The end user can select a button to update the page with the latest Mission to Mars headline and feature image. 

Key Deliverables
Step One: Four “Scrapes” from the following:
1.	NASA Mars News
    a.	  Reference the NASA Mars News Site at (https://mars.nasa.gov/news/) 
    b.	  The latest News Title and Paragraph Text is collected
    c.	  The text is converted to variables and inserted into a MongoDB dictionary that are referenced later
2.	JPL Mars Space Images - Featured Image
    a.	  The JPL Featured Space Image at (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars.) is referenced for a changing image to be utilized as the feature image
    b.	  Splinter is utilized to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
      	  The full size `.jpg` image is utilized
    c.	  The imaged is converted to variables and inserted into a MongoDB dictionary that are referenced later
3.	Mars Facts
    a.	  The Mars Facts webpage at (https://space-facts.com/mars/) is used to collect a table containing facts about the planet. Pandas is utilized to scrape the table containing facts about the planet including Diameter, Mass, etc.
    b.	  Pandas is utilized to convert the data to a HTML table string to be referenced later
4.	Mars Hemispheres
    a.	  The USGS Astrogeology site at (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) is referenced to obtain high resolution images for each of Mar's hemispheres.
    b.	  A script was created that clicks each of the links to the hemispheres in order to find the image url to the full resolution image.
    c.	  Both an image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name are stored as a list of dictionaries in                MongoDB to be referenced later.
Step Two: Deliver the scrapped information via an HTML page
    1.	MongoDB and Flask templating were used to create a new HTML page that displays all of the information that was scraped from the URLs above.
    2.	Jupyter notebook was utilized to plan and test the Python script called `scrape_mars.py`. 
    3.	A function was created in Visual Studio to execute all of the scraping code from above and return one Python dictionary in MongoDB containing all of the scraped data.
    4.	A route called `/scrape` that imports the `scrape_mars.py` script and calls the `scrape` function was crated in app.py to enable the application. 
    5.	Scraped text, tables and images are saved to Mongo as a Python dictionary.
    6.	A main route `/` queries the Mongo database and passes the mars data into an HTML template to display the data to the end consumer.
    7.	An HTML template file called `index.html` takes the mars data dictionary and display all of the data in the appropriate HTML elements. 

Topline (3 Key) Takeaways
1.	This was a technical challenge versus an analytical challenge
2.	Scrapping can be a tedious process but useful if there is value in accessing changing information available on the web. 
3.	The nuances of flask templating, how styling is achieved when utilizing flask proved challenge.

Visuals
Please reference the project “pitchbook” for screen shot examples. 

Installation
The project was completed using multiple support tools including: Visual Studio, Jupyter Notebook, Python, HTML, CSS, Bootstrap, MongoDB and various websites. 

Support
Please reference the Denver University GitLab repository for class materials and instructions.

Roadmap
Not applicable

Contributing
I consumed several hours of TA and tutor time to complete the project. 

Authors and acknowledgment
Again, great class structure, good after class and tutor support. 

License
Not applicable

Project status
Project objectives and deliverables achieved were achieved. 
