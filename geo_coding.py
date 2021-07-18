import googlemaps
import database_connection
import sqlite3

connect_database = sqlite3.connect('database_address.db')
cur = connect_database.cursor()

gmaps = googlemaps.Client(key= 'AIzaSyAetuK912epZTR2lG2od8nC8lKlSj39GVo')
def address_add():
    address_input = input("inserisci lindirizzo")
    cur.execute(INSERT )


#def address_fetch():
    #cur.execute('''FROM address SELECT street''')


geo_code_result = gmaps.geocode()
