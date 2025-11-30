from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
DRIVER_PATH    = "/Python/chromedriver.exe"
URL = "https://www.bcit.ca/study/programs/5512cert#courses"
# "https://www.rottentomatoes.com/browse/tv_series_browse/sort:popular"
#'https://www.rottentomatoes.com/critics/source/268'
# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(service=Service(DRIVER_PATH))
    browser.get(URL)
    time.sleep(3)
    # content = browser.find_elements(By.CSS_SELECTOR, ".publication-link span")
    content = browser.find_elements(By.CSS_SELECTOR,".clicktoshow")
    for e in content:
        start = e.get_attribute('innerHTML')
        # Beautiful soup allows us to remove HTML tags from our content if it exists.
        soup = BeautifulSoup(start, features="lxml")
        print(soup.get_text())
        print("***")  # Go to new line.

    # print("The path to webdriver_manager was found.")
# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'DRIVER_PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())
