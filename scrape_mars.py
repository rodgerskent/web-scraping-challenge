# Rodgers Scrape Script
import os
import pymongo
import requests
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser

def scrapemars():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    links = browser.find_by_css('a.product-item h3')
    hemisphere_image_url =[]

    for i in range(len(links)):
        hemisphere = {}
            
        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
        
        # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
    
        # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
        
        # Append hemisphere object to list
        hemisphere_image_url.append(hemisphere)
        
        # Finally, we navigate backwards
        browser.back()
     
        #browser.quit()

    print(hemisphere_image_url[0]["img_url"])

    return hemisphere_image_url
