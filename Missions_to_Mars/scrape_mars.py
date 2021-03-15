# Import BeautifulSoup
from bs4 import BeautifulSoup 

# Import Splinter and set the chromedriver path
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import requests
import pymongo
import time
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_data_dict = {}

    # start -- insert jupyter notebok code here 

    # ------------------------------------------
    # - NASA Mars News Site
    # ------------------------------------------

    # Visit the following URL
    url = 'https://mars.nasa.gov/news'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #soup

    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())

    # Scrape the NASA Mars News Site and collect the latest 
    # News Title and Paragraph Text.
    # Assign the text to variables that you can reference later.

    # Get the latest News Title and Paragraph Text.
    news_title = soup.find_all('div', class_ = 'content_title')[0].text
    news_title

    news_paragraph = soup.find_all('div', class_ = 'article_teaser_body')[0].text
    news_paragraph

    # ------------------------------------------
    # - JPL Mars Space Images - Featured Image
    # ------------------------------------------

    # Visit the following URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #soup

    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #soup

    # find all images
    for item in soup.find_all('img'): 
        print(item['src'])

    # url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    result = url.find('index.html') 
    print(result)
    root = url[0:result]

    # Retrieve featured image link
    relative_image_path = soup.find_all('img')[1]["src"]
    featured_image_url = root + relative_image_path
    featured_image_url

    relative_image_path

    # ------------------------------------------
    # - Mars Facts
    # ------------------------------------------
    # Visit the following URL
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #soup

    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())

    # Scrape the table containing facts about the planet (Mars) including Diameter, Mass, etc.
    mars_facts_table = pd.read_html(url)
    mars_facts_table

    mars_df = mars_facts_table[2]
    mars_df

    # rename columns (0 = Desc, 1 = Value)
    mars_df.columns = ["Desc", "Value"]
    mars_df

    # save table as html file named: data_table.html
    mars_df.to_html("mars_data.html")  

    # assign it to a variable (string) 
    html_mars_table = mars_df.to_html()
    html_mars_table

    # ------------------------------------------
    # - Mars Hemispheres
    # ------------------------------------------
    # Visit the following URL  -- USGS Astrogeology site 
    root_url = 'https://astrogeology.usgs.gov'
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #soup

    # Examine the results, then determine element that contains sought info
    #print(soup.prettify())

    # Mars hemispheres & image URLs 
    mars_hemispheres = soup.find('div', class_='collapsible results')
    all_mars_hemispheres = mars_hemispheres.find_all('div', class_='item') 

    # Store the urls in an array
    hemisphere_img_urls = []

    # Iterate through each hemisphere and collect data
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing 
    # the hemisphere name.

    for x in all_mars_hemispheres:
        hemisphere_link = mars_hemispheres.a["href"]
    
        #Click each of the links to the hemispheres in order to find the image url to the full resolution image.
        hemisphere = x.find('div', class_="description")
        h_title = hemisphere.h3.text   
        h_link = hemisphere.a["href"]    
        browser.visit(root_url + h_link)        
        img_html = browser.html
        img_soup = BeautifulSoup(img_html, 'html.parser')  
        img_link = img_soup.find('div', class_='downloads')
        img_url = img_link.find('li').a['href']
    
        # Use a Python dictionary to store the data using the keys img_url and title.
        mars_image_dict = {}
        mars_image_dict['title'] = h_title
        mars_image_dict['img_url'] = img_url        
        hemisphere_img_urls.append(mars_image_dict)      

    # display urls
    #hemisphere_img_urls

    # store data in Mars dictionary
    mars_data_dict = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image_url": featured_image_url,
        "fact_table": str(html_mars_table),
        "hemisphere_images": hemisphere_img_urls
    }

    # display Mars dictionary
    #mars_data_dict
    
    # end of jupyter notebok code 
 
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data_dict
