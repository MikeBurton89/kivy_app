import googlemaps
import database_connection
import sqlite3
#connect to the database in the folder
connect_database = sqlite3.connect('database_address.db')

cur = connect_database.cursor()

gmaps = googlemaps.Client(key= '#there should be a googlemaps API key')

#this function should add the address to the database. Needs to be expanded to ask for name of the place and other infos
def address_add():
    address_input = input("What's the address?")
    cur.execute(INSERT INTO address VALUES(address_input)
    cur.commit()

# this function should fetch the address so that it can be used to geocode it
#def address_fetch():
    #cur.execute('''FROM address SELECT street''')


geo_code_result = gmaps.geocode()
