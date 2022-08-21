from __future__ import absolute_import, unicode_literals

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from celery.utils.log import get_task_logger

from djbookville.celery import app

import time

logger = get_task_logger(__name__)

@app.task(name="tasks.IsbnNlg")
def IsbnNlg(isbn):
    
    print('connected to task')
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Firefox(options=options)
    print('got web driver')
    time.sleep(.25)
    driver.get('https://isbn.nlg.gr/index.php?search_type_asked=search_nlg_books')
    print('connected to nlg')
    time.sleep(0.25)
    
    find_field = driver.find_element(By.XPATH,"//input[@id='isbn_from']")
    find_field.click()

    time.sleep(0.25)

    
    if len(isbn) == 13:
        if isbn[3:6] == '618':
            find_select = Select(driver.find_element(By.ID, "sel_isbn_class"))
            find_select.select_by_value("618")
            print('selected value')

            isbn_ready = isbn[6:13]
        elif isbn[3:6] == '960':
            find_select = Select(driver.find_element(By.ID, "sel_isbn_class"))
            find_select.select_by_value("960")
            print('selected value')

            isbn_ready = isbn[6:13]
        else:
            isbn_ready = "0000000" 

    find_field.send_keys(isbn_ready)

    find_button = driver.find_element(By.CLASS_NAME,"btn-primary")
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
            title = td_tags[1]
            print(f'got title! {title}')
            info['title'] = title
            driver.close()
        except TimeoutError:
            logger.info('Timeout error occured 1')
            driver.quit()
    except TimeoutError:
        logger.info('Timeout error occured 2')
        driver.quit()

    return info

@app.task(name="tasks.IsbnPoliteia")
def IsbnPoliteia(isbn):
    
    print('connected to task')
    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Firefox(options=options)
    print('got web driver')
    
    driver.get('https://www.politeianet.gr/search')
    print('connected to politeianet')
    time.sleep(0.25)
    
    find_isbn_field = driver.find_element(By.NAME,"isbn")
    print('found isbn field')
    find_isbn_field.click()

    find_isbn_field.send_keys(isbn)

    time.sleep(.1)

    find_submit_button = driver.find_element(By.CLASS_NAME,'btSubmit')
    find_submit_button.click()

    try:
        WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.ID, "product_list")))
        find_title = driver.find_element(By.CLASS_NAME,'browse-product-title')
        find_title.click()

        try:
            logger.info(f'successfully retriever data for {isbn}')
            WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.ID, "maincol2")))
            info_div = driver.find_element(By.CLASS_NAME,'product-type')
            tds = info_div.find_elements(By.TAG_NAME,'td')
            for x in tds:
                print(x)

        except TimeoutError:
            logger.info('Timeout error occured 1')
            driver.quit()

    except TimeoutError:
        logger.info('Timeout error occured 1')
        driver.quit()


    return info

