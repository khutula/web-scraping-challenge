# GT Bootcamp Web Scraping Homework: Mission to Mars

## Table of Contents
1. [Introduction](#introduction)
2. [Objectives](#objectives)
3. [Technologies & Sources](#technologies)
4. [Files](#files)

<a name="introduction"></a>
### Introduction
In this assignment, I have been tasked with creating a responsive website that shows off analysis from a preivous project. I elected to use the provided images/dataset for this assignment.

<a name="objectives"></a>
### Objectives
Create a responsive website launched in GitHub pages that has:
* Navigation menu created using Bootstrap
* Landing Page describing the project and linking to plot pages
* Plot Pages for each plot that shows a large image of the plot and describes its significance
* Comparison Page showing all four plots enlarged with Bootstrap
* Data page showing all data in a table and displayed with Bootstrap classes for responsiveness

<a name="technologies"></a>
### Technologies & Sources
This project uses: 
* Python Version 3.6.13
* Jupyter Notebook Version 6.1.4
* Bootstrap Version 4.3.1
* Flask Version 1.1.2
* BeautifulSoup
* Splinter
* WebDriver_Manager
* PyMongo
* Mongo Version 5.0.2

<a name="files"></a>
### Files

* [Flask Application](Missions_to_Mars/app.py): Python script containing code for the Flask Application to run both the home page, actively scrape data, and store data in a Mongo Database for retrieval
* [Web Scraping Script](Missions_to_Mars/scrape_mars.py): Python script containing code to scrape all websites and return results as a dictionary
* [Web Scraping Test File](Missions_to_Mars/mission_to_mars.ipynb): jupyter notebook file containing all code used in the [Web Scraping Script](Missions_to_Mars/scrape_mars.py)
* [Webpage](Missions_to_Mars/templates/index.html): HTML written for the home page to include information from [Web Scraping Script](Missions_to_Mars/scrape_mars.py)

#### Screenshot of Top Portion of Web Page
![Top of Web Page](top_of_webpage.PNG)

#### Screenshot of Bottom Portion of Web Page
![Bottom of Web Page](bottom_of_webpage.PNG)