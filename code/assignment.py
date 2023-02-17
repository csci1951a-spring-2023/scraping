from bs4 import BeautifulSoup
import requests
import sqlite3

### IEX TRADING API METHODS ###
IEX_TRADING_URL = "https://cloud.iexapis.com/stable/stock/"


### YAHOO FINANCE SCRAPING
MOST_ACTIVE_STOCKS_URL = "https://cs1951a-s21-brown.github.io/resources/stocks_scraping_2021.html"

### Register at IEX to receive your unique token
TOKEN = ''

# TODO: Use BeautifulSoup and requests to collect data required for the assignment.

# TODO: Save data below.

#TODO: Use IEX trading API to collect sector and previous pricing data.

# Create connection to database

#Make sure you have the right path to data.db, in case you have any connection issues
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Delete tables if they exist
c.execute('DROP TABLE IF EXISTS "companies";')
c.execute('DROP TABLE IF EXISTS "quotes";')

#TODO: Create tables in the database and add data to it. REMEMBER TO COMMIT
