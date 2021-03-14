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









    # end of jupyter notebok code 
 

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data_dict
