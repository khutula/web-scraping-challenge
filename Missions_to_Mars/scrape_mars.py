# Import Dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.firefox import GeckoDriverManager

def scrape():
    # open browser in Firefox
    executable_path = {"executable_path": GeckoDriverManager().install()}
    browser = Browser('firefox', **executable_path, headless=False)


    ############### NASA Mars News ###############

    # visit Mars News website and take HTML code
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html=browser.html

    # convert HTML to BeautifulSoup
    soup = bs(html, "html.parser")

    # locate most recent article title and paragraph
    news_title = soup.body.find("div", class_="content_title").text.strip()
    news_p = soup.body.find("div", class_="article_teaser_body").text.strip()


    ############### JPL Mars Space Images - Featured Image ###############

    # visit Mars Space Images website and take HTML code
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html

    # convert HTML to BeautifulSoup
    soup = bs(html, "html.parser")

    # parse for the featured image source
    featured_image = soup.body.find("img", class_="headerimage")["src"]

    # append entire url with featured image source
    featured_image_url = url + featured_image


    ############### Mars Facts ###############

    # visit Mars Space Images website using pandas and take HTML code
    url = "https://galaxyfacts-mars.com/"
    mars_facts = pd.read_html(url)

    # specify table to target, rename columns, and set index
    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = mars_facts_df.iloc[0]
    mars_facts_df = mars_facts_df.drop(mars_facts[0].index[0])
    mars_facts_df = mars_facts_df.set_index("Mars - Earth Comparison")

    # convert dataframe back to html
    mars_facts_html = mars_facts_df.to_html(classes="table table-striped table-dark")


    ############### Mars Hemispheres ###############

    # visit Mars Hemispheres website and take HTML code
    base_url = "https://marshemispheres.com/"
    browser.visit(base_url)
    html = browser.html

    # convert HTML to BeautifulSoup
    soup = bs(html, "html.parser")

    # use BeautifulSoup to find all div with specified class
    div_list = soup.body.find_all("div", class_="description")

    # create empty list
    sites = []

    # cycle through each div returned
    for div in div_list:
        
        # find the a element with specified class in the div element and pull the data for href to get the end location for the full image
        site = div.find("a", class_="product-item")["href"]
        
        # append site href to list
        sites.append(site)

    # create empty list to store dictionaries
    hemisphere_image_urls = []

    # cycle through each site href
    for site in sites:
        try:
            
            # visit specifichemisphere page and take HTML code
            url = base_url + site
            browser.visit(url)
            html = browser.html
            
            # convert HTML to BeautifulSoup
            soup = bs(html, "html.parser")
            
            # use BeautifulSoup to find image with specified class and access source of image
            img_url_ending = soup.body.find("img", class_="wide-image")["src"]
            
            # add base url to the image source to get full url
            img_url = base_url + img_url_ending
            
            # use title on page, removing unneeded trailing " Enhanced" to get title
            title = soup.body.find("h2", class_="title").text.strip()[:-9]
            
            # append dictionary of information to list
            hemisphere_image_urls.append({"title": title, "img_url": img_url})
        except Exception as e:
            print(e)


    ############### Quit Browser ###############
    browser.quit()


    ############### create one dictionary for return of all scraped info ###############

    scraped_data = {
        "NewsTitle": news_title,
        "NewsParagraph": news_p,
        "FeaturedImage": featured_image_url,
        "MarsFactsTable": mars_facts_html, 
        "HemisphereImages": hemisphere_image_urls
    }

    return scraped_data