from __future__ import absolute_import, unicode_literals

from celery import shared_task

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from celery.utils.log import get_task_logger

import time

logger = get_task_logger(__name__)

@shared_task(name="SendIsbnEthnikiVivliothiki")
def SendIsbnEthnikiVivliothiki(isbn):

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)
    
    driver.get('https://isbn.nlg.gr/index.php?search_type_asked=search_nlg_books')

    time.sleep(0.25)
    
    find_field = driver.find_element(By.XPATH,"//input[@id='isbn_from']")
    find_field.click()

    time.sleep(0.25)

    
    if len(isbn) == 13:
        if isbn[3:6] == '618':
            find_select = Select(driver.find_element(By.XPATH, "//select[@id=sel_isbn_class]"))
            find_select.select_by_value("618")

            isbn_ready = isbn[6:13]
        elif isbn[3:6] == '960':
            find_select = Select(driver.find_element(By.XPATH, "//select[@id=sel_isbn_class]"))
            find_select.select_by_value("960")

            isbn_ready = isbn[6:13]
        else:
            isbn_ready = "0000000" 

    find_field.send_keys(isbn_ready)

    find_button = driver.find_element(By.CLASS_NAME,"btn btn-primary")
    find_button.click()

    time.sleep(0.25)

    try:
        plus_icon = WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.ID, "el411040Img")))
        plus_icon.click()
        try:
            logger.info(f'successfully retriever data for {isbn}')

            table = WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.ID, "el411040Img")))
            
            # find_title = driver.find_element(By.XPATH, "//span[@class='public_title']")
            
            td_tags = driver.find_elements(By.TAG_NAME, "td")
            info = {}
            title = td_tags[1].innerHtml
            info['title'] = title
        except TimeoutError:
            logger.info('Timeout error occured 1')
            driver.quit()
    except TimeoutError:
        logger.info('Timeout error occured 2')
        driver.quit()

    return info

