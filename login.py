#-*-coding: utf-8 -*-

# packages
import xmlrpc.client as xmlrpc_client


# switch
USE_ODOO_DEMO = False

# server url
URL = "https://studio-slide.odoo.com"
URL_ODOO_DEMO = "https://demo.odoo.com"

if USE_ODOO_DEMO:
    URL_START = f"{URL_ODOO_DEMO}/start"

    COMMON_URL = f"{URL_ODOO_DEMO}/xmlrpc/2/common"

else:
    URL_START = f"{URL}/start"

    COMMON_URL = f"{URL}/start"

# database name
DB = "studio-slide"

# username
USERNAME = "nathanbangwa.exonus@gmail.com"
PASSWORD = "Wmn@NB#07"

API_KEY = "68ac473480a0d82770d9236f350d377f94569341"

def test_database():

    info = xmlrpc_client.ServerProxy(URL_START).start()

    print (f"[test_database.info] : {info}")

    return info

def test_logging_in():

    common = xmlrpc_client.ServerProxy(COMMON_URL)

    return common



