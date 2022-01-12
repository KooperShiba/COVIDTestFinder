from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time
import random

def bruteForceWalmart(browser):
    maxAttempts = 10
    halt = 4

    print(f"Attempting automated brute force with {maxAttempts} attempts...")

    # xpathStoreNamePre = '/html/body/div[3]/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div['
    # xpathStoreNamePost = ']/label/div/span[1]'

    for i in range(maxAttempts):
        xpathPickupAt = '//*[@id="__next"]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/div[2]/button'
        WebDriverWait(browser, halt).until(
            EC.presence_of_element_located((By.XPATH, xpathPickupAt))
        )
        button = browser.find_element(By.XPATH, xpathPickupAt)
        button.click()

        xpathRadioPre = '/html/body/div[3]/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div['
        xpathRadioPost = ']/label/input'

        xpathRadio = xpathRadioPre + str(random.randint(1, 6)) + xpathRadioPost
        WebDriverWait(browser, halt).until(
            EC.presence_of_element_located((By.XPATH, xpathRadio))
        )
        button = browser.find_element(By.XPATH, xpathRadio)
        button.click()
        time.sleep(halt)

        xpathSave = '/html/body/div[3]/div/div[3]/div[1]/div/div[3]/div/button'
        button = browser.find_element(By.XPATH, xpathSave)
        button.click()

        try:
            xpathCheckAvailabilityNearby = '//*[@id="__next"]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div/section/div/button'
            WebDriverWait(browser, halt).until(
                EC.presence_of_element_located((By.XPATH, xpathCheckAvailabilityNearby))
            )
            print("Brute force successful")
            time.sleep(halt)
            return True
        except TimeoutException:
            pass
    print("Brute force failed")
    return False





def getTargetStock2(browser, fullTargetURL, zipCodes):
    delay = 4
    allStoresInStock = set()
    browser.get(fullTargetURL)

    try:
        xpathCheckOtherStores = '//*[@id="viewport"]/div[4]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/button'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathCheckOtherStores))
        )
        #print("Target Page loaded")
        button = browser.find_element(By.XPATH, xpathCheckOtherStores)
        button.click()
        # print("Clicked 'Check Other Stores'")

        xpathNextClosestInStock = '/html/body/div[7]/div/div/div[2]/div/div/div/div/div[6]/div/span'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathNextClosestInStock))
        )
    except TimeoutException:
        xpathEditStore = '//*[@id="viewport"]/div[4]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[2]/div/button'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathEditStore))
        )
        # print("Target Page loaded")
        button = browser.find_element(By.XPATH, xpathEditStore)
        button.click()

        # print("Clicked 'Check Other Stores'")
        xPathCheckOtherStores = '/html/body/div[7]/div/div/div[2]/div/div/div/div/div[1]/h2'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xPathCheckOtherStores))
        )



    for zip in zipCodes:

        #Edit your location
        try:
            xPathEditYourLocation = "/html/body/div[7]/div/div/div[2]/div/div/div/div/div[3]/a"
            button = browser.find_element(By.XPATH, xPathEditYourLocation)
            button.click()
        except NoSuchElementException:
            xPathEditYourLocation = "/html/body/div[7]/div/div/div[2]/div/div/div/div/div[2]/a"
            button = browser.find_element(By.XPATH, xPathEditYourLocation)
            button.click()

        #Put in zip code to box
        xPathStoreSearch = '//*[@id="storeSearch"]'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xPathStoreSearch))
        )
        time.sleep(random.randint(1,2))
        textBox = browser.find_element(By.XPATH, xPathStoreSearch)
        textBox.click()

        for i in range(5):
            textBox.send_keys(Keys.BACK_SPACE)
        textBox.send_keys(zip)

        try:
            xPathFindStores = "/html/body/div[7]/div/div/div[2]/div/div/div/div/div[4]/div/div/div/div/div[2]/div[1]/div/button"
            button = browser.find_element(By.XPATH, xPathFindStores)
            button.click()
        except NoSuchElementException:
            xPathFindStores = "/html/body/div[7]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/button"
            button = browser.find_element(By.XPATH, xPathFindStores)
            button.click()

        # print("All store stock is loaded")
        xpathStoreCardPre = '/html/body/div[7]/div/div/div[2]/div/div/div/div/div['
        xpathStoreCardPost = ']/div/h3/span[1]'
        xpathStoreCardPostAvailabilityText = ']/div/div[1]/div/div[1]/span'
        xpathStoreCardStartI = 6
        numStores = 26

        for i in range(xpathStoreCardStartI, xpathStoreCardStartI + numStores):
            try:
                xPathCombined = xpathStoreCardPre + str(i) + xpathStoreCardPostAvailabilityText
                store = browser.find_element(By.XPATH, xPathCombined)
                storeStock = store.text
                if storeStock in ('In stock', 'Limited stock'):
                    xPathCombined = xpathStoreCardPre + str(i) + xpathStoreCardPost
                    store = browser.find_element(By.XPATH, xPathCombined)
                    storeName = store.text
                    allStoresInStock.add(f"{storeName} - {storeStock}")
            except NoSuchElementException:
                pass
    # print("Completed loading stock")
    return allStoresInStock


def WALMART():
    # WALMART

    WALMART_MISSING_BUTTON_FLAG = False

    print("CHECKING WALMART FOR STOCK")
    print(stockText + "BinaxNOW COVID‐19 Antigen Self Test (2 Count)")
    browser.get("https://www.walmart.com/ip/BinaxNOW-COVID-19-Antigen-Self-Test-2-Count/142089281")
    delay = 4

    # Bot Check
    try:
        xpathWalmartBotCheck = '//*[@id="message"]'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathWalmartBotCheck))
        )
        message = browser.find_element(By.XPATH, xpathWalmartBotCheck)
        if message.text == "Activate and hold the button to confirm that you’re human. Thank You!":
            print()
            print("HUMAN VERIFICATION DETECTED /!\\")
            print("Need manual intervention...")
            input("Press [ENTER] when Anti-BOT verification is completed")
            print("Resuming script...")
            print()
    except TimeoutException:
        pass

    # click on check availability nearby
    try:
        xpathCheckAvailabilityNearby = '//*[@id="__next"]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div/section/div/button'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathCheckAvailabilityNearby))
        )
        button = browser.find_element(By.XPATH, xpathCheckAvailabilityNearby)
        button.click()
    except TimeoutException:
        print()
        print("Missing CHECK FOR AVAILABILITY button. Walmart may have dynamically changed page.")

        if not bruteForceWalmart(browser):
            print("Try selecting at different locations under 'Pickup at [LOCATION]'")
            input("Press [ENTER] to continue...")
            print("Resuming script...")
        print()
        xpathCheckAvailabilityNearby = '//*[@id="__next"]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div/section/div/button'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathCheckAvailabilityNearby))
        )
        button = browser.find_element(By.XPATH, xpathCheckAvailabilityNearby)
        button.click()
        WALMART_MISSING_BUTTON_FLAG = True

    # wait until select store shows up
    xpathSaveBox = '/html/body/div[3]/div/div[3]/div[1]/div/div[3]/div/button'
    if WALMART_MISSING_BUTTON_FLAG:
        xpathSaveBox = '/html/body/div[2]/div/div[3]/div[1]/div/div[3]/div/button'
    WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((By.XPATH, xpathSaveBox))
    )

    # Look for "Available at this store"
    # '/html/body/div[3]/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div[1]/label/div/span[1]'
    xpathStoreNamePre = '/html/body/div[3]/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div['
    if WALMART_MISSING_BUTTON_FLAG:
        xpathStoreNamePre = '/html/body/div[2]/div/div[3]/div[1]/div/div[2]/div/div/div/div[2]/div['
    xpathStoreNamePost = ']/label/div/span[1]'
    xpathStoreStockPost = ']/label/div/span[4]/span'
    xpathStoreAddressPost = ']/label/div/span[2]'

    allInStockStores = set()
    for zip in zipcodes:
        # Find zipcode box
        xpathZipcodeBox = '/html/body/div[3]/div/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/input'
        if WALMART_MISSING_BUTTON_FLAG:
            xpathZipcodeBox = '/html/body/div[2]/div/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/input'

        textBox = browser.find_element(By.XPATH, xpathZipcodeBox)
        textBox.click()
        for i in range(5):
            textBox.send_keys(Keys.BACK_SPACE)
        textBox.send_keys(zip)

        xpathSaveBox = '/html/body/div[3]/div/div[3]/div[1]/div/div[3]/div/button'
        if WALMART_MISSING_BUTTON_FLAG:
            xpathSaveBox = '/html/body/div[2]/div/div[3]/div[1]/div/div[3]/div/button'
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpathSaveBox))
        )
        time.sleep(2)

        for i in range(1, 6):
            xpathStoreName = xpathStoreNamePre + str(i) + xpathStoreNamePost
            xpathStoreStock = xpathStoreNamePre + str(i) + xpathStoreStockPost
            xpathStoreAddress = xpathStoreNamePre + str(i) + xpathStoreAddressPost

            storeStockStatus = browser.find_element(By.XPATH, xpathStoreStock)
            if storeStockStatus.text == "Available at this store":
                storeName = browser.find_element(By.XPATH, xpathStoreName)

                storeAddress = browser.find_element(By.XPATH, xpathStoreAddress)
                allInStockStores.add(f"Available at this store - {storeName.text} - {storeAddress.text}")

    print()
    print("CHECKING WALMART FOR STOCK")
    print(stockText + "BinaxNOW COVID‐19 Antigen Self Test (2 Count)")
    for x in allInStockStores:
        print(x)
    time.sleep(random.randint(2, 4))

def TARGET():
    #TAGRET
    print("CHECKING TARGET FOR STOCK")

    print(stockText + "ellume COVID-19 Rapid Antigen Home Test")
    url = "https://www.target.com/p/ellume-covid-19-rapid-antigen-home-test/-/A-83685429#lnk=sametab"
    storesInStock = getTargetStock2(browser, url, zipcodes)
    if len(storesInStock) == 0:
        print("No stock available around all zip codes")
    else:
        for store in storesInStock:
            print(store)
    print()
    time.sleep(random.randint(minWaitTime, maxWaitTime))

    print(stockText + "Access Bio Covid Rapid Test - 2ct")
    url = "https://www.target.com/p/access-bio-covid-rapid-test-2ct/-/A-84602542#lnk=sametab"
    storesInStock = getTargetStock2(browser, url, zipcodes)
    if len(storesInStock) == 0:
        "No stock available around all zip codes"
    else:
        for store in storesInStock:
            print(store)
    print()
    time.sleep(random.randint(minWaitTime, maxWaitTime))

    print(stockText + "FlowFlex Covid-19 Antigen Home Test")
    url = "https://www.target.com/p/flowflex-covid-19-antigen-home-test/-/A-84996289#lnk=sametab"
    storesInStock = getTargetStock2(browser, url, zipcodes)
    if len(storesInStock) == 0:
        "No stock available around all zip codes"
    else:
        for store in storesInStock:
            print(store)
    print()
    #time.sleep(random.randint(minWaitTime, maxWaitTime))



if __name__ == '__main__':
    print('COVID TESTS STOCK')

    minWaitTime = 2
    maxWaitTime = 6

    zipcodesCO = {"80013", "80123", "80002", "80020", "80523", "80903", "80226", "80204"}
    zipcodesCA = {"92544", "90630", "90404", "92223", "92545", "90210", "90210", "92691", "91910", "91911"}
    zipcodesNorCA = {"95051", "95131", "95148"}

    zipcodes = zipcodesCO
    print("Checking around the following zip codes:" + str(zipcodes))

    random.seed(time.time())
    stockText = "Checking stock for: "
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument('--disable-blink-features=AutomationControlled')

    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    try:
        WALMART()
        print()
        TARGET()

    finally:
        browser.quit()

