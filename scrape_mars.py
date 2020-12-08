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
    
    # Feature Text Scrape
    url1 = 'https://mars.nasa.gov/news/'
    response = requests.get(url1)
    browser.visit(url1)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    slide_elem = soup.select_one('ul.item_list li.slide')
    title = slide_elem.find('div', class_='content_title').get_text()
    paragraph = slide_elem.find('div', class_="rollover_description_inner").get_text()
    featuretext = {}
    featuretext["feature_title"]=title
    featuretext["feature_paragraph"]=paragraph
    browser.back()
    
    # Table Scrape
    url2 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url2)
    df = tables[0]
    df = df.rename(columns={0: " ", 1: "Mars"})
    df = df.set_index(" ")
    # Add either column name here and/or set index to eliminate the left index numbers
    featuretext["feature_table"]=df.to_html()
    browser.back()

    # Feature Image Scrape
    url3 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url3)
    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')
    images=soup3.select_one('article', class_="button fancybox").get("style")[23:75]
    imagesurl=f'https://www.jpl.nasa.gov{images}'
    featuretext["feature_image"]=imagesurl
    browser.back()

    # Hemisphere Scape
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

    # print(hemisphere_image_url[0]["img_url"])
    featuretext["hemisphere_list"]=hemisphere_image_url

    browser.quit()
    return featuretext
