from bs4 import BeautifulSoup
from splinter import Browser
import selenium
import requests
import shutil
import pandas as pd
from IPython.display import Image
import time


def init_browser():
    executable_path = {"executable_path": "C:/webdrive/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    article = soup.find("div", class_="list_text")
    news_p = article.find("div", class_="article_teaser_body").text
    news_title = article.find("div", class_="content_title").text
    news_date = article.find("div", class_="list_date").text

    mars_data["news_date"] = news_date
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p

    url2 = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    img_name = soup.find("img", class_="thumb")["alt"].replace(" ", "_")

    img_url = "https://jpl.nasa.gov"+image
    featured_image_url = img_url

    mars_data["featured_image_url"] = featured_image_url

    response = requests.get(img_url, stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    Image(url='img.jpg')
    url_twitt = 'https://twitter.com/marswxreport?lang=en'

    # Launch browser
    browser.visit(url_twitt)
    results = {}
    # Create beautifulsoup object
    soup = BeautifulSoup(browser.html, 'html.parser')

    # localate the first tweet and extract text from it
    mars_weather = soup.find('div', class_='js-tweet-text-container').text.split('\n')[1]
    results['mars_weather'] = mars_weather

    mars_data["mars_weather"] = mars_weather

    # Facts
    url_facts = 'https://space-facts.com/mars/'
    browser.visit(url_facts)


    grab = pd.read_html(url_facts)
    mars_data = pd.DataFrame(grab[0])
    mars_data.columns = ['Mars','Data']
    mars_table = mars_data.set_index("Mars")
    marsdata = mars_table.to_html(classes='marsdata')
    marsdata = marsdata.replace('\n', ' ')

    mars_data["mars_table"] = marsdata


    # Mars Hemispheres

    url_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hemispheres)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_hemis=[]

    for i in range(4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2", class_="title").text
        img_url = 'https://astrogeology.usgs.gov' + partial
        dictionary = {"title": img_title, "img_url": img_url}
        mars_hemis.append(dictionary)
        browser.back()

    mars_data['mars_hemis'] = mars_hemis
    print(mars_data)
    return mars_data
