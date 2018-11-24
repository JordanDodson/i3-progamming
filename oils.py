# Program to see if there are hydrogenated oil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# These packages will help us act like a human.
import time
import random

# This is for reading and writing CSV (comma-separated value) files.
import csv

def pause():
    """Call this function to pause for just a moment, like a human, instead of plunging forward."""
    time.sleep(abs(random.gauss(1.032028, 0.4983)))

def minipause():
    """Use this one for a short pause"""
    time.sleep(abs(random.gauss(.04398, 0.0231)))

    #get the peanut butter names

    def getpb():
        """Gets our zipcodes from the file"""
        with open('pbs.txt') as f:
            zips = [i.strip() for i in f.readlines()]

        for

    return zips

def visitwall():
    """Visits the Wall and returns a browser"""
    # chromedriver must be in the same folder as this file.
    browser = webdriver.Chrome('./chromedriver')

    # Now that we have a robo-browser, we can robo-visit a given link.
    browser.get('https://www.walmart.com/')

    return browser

def getsearchbar():
    """Finds the search bar and returns it."""
    return browser.find_element_by_xpath('//*[@id="global-search-input"]')

    #//*[@id="searchProductResult"]/ul/li[1]/div/div[2]/div[2]/div/div/a/img
def clickfirstresult():
    # Click the Store Availability button
    browser.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[1]/div/div[2]/div[2]/div/div/a/img').click()

def searchforpeanutbutter():
    # QUICK, ACT HUMAN
    pause()

    # Okay, coast is clear. Get the searchbar.
    searchbar = getsearchbar()

    # Look for peanut butter
    searchbar.send_keys(zips[0])

    # Pretend to search for the enter key
    minipause()

    # Pretend you have found it.
    searchbar.send_keys(Keys.ENTER)


    def getproductinfo(productinfo):
        """Extracts and returns product information from the text in a search result."""
        infolist = productinfo.split('\n')

        # Get the product's name
        productname = infolist[2]

        # Quit the browser.
        browser.quit()

        # Pretend to reflect on what you have done.
        pause()
        #hydrogenated


    # Get the products in each zipcode
    for currentzip in zips:

        # Visit the Wall
        browser = visitwall()

        # Search for peanut butter
        searchforpeanutbutter()

        # Set the zipcode,
        print("Setting zip to " + currentzip)

        # Get all products on page
        for i in list(range(1, 200)):

            try:
                print("Grabbing product " + str(i))
                product = browser.find_element_by_xpath('//*[@id="searchProductResult"]/ul/li[' + str(i) + ']')
            except:
                # If there is an exception we assume there are no more products.
                print("No such product!")
                break

            name, price, available = getproductinfo(product.text)

            # Put that product in the CSV. "a" is editing
            with open('out.csv','a') as f:
                w = csv.writer(f)

                try:
                    row = [currentzip, name, price, available]
                    w.writerow(row)
                except:
                    import pdb; pdb.set_trace()
