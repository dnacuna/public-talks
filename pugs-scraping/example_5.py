
from time import sleep
from selenium import webdriver

# start up a chrome
driver = webdriver.Chrome()

# load our target page
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

# find the download button and click
button = driver.find_element_by_name('ctl00$MainContentHolder$TabStrip1$Download_0')
button.click()

# sleep for demo purposes
sleep(15)
driver.quit()
