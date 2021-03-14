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








    # end of jupyter notebok code 
 

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data_dict
