import sqlite3
import os

'''
        The report database has:
            - an ID, used for something in SQLite (idk)
            - A google place ID of the parent restaurant it was made for
            - The current time the report was made, measured in seconds since 1/1/1970
            - The name of the menu item the user reported

        The restaurant database has:
            - The same ID mentioned above
            - The google place ID of itself
            - The name of the restaurant
            - A comma separated string of its menu items
'''

class DatabaseHelper:
    
    def __init__(self):
        self.REPORTS_FILE_NAME = "reports.db"
        self.reports_id = 1

        self.RESTAURANTS_FILE_NAME = "restaurants.db"
        self.restr_id = 1

    def open(self, db):
        return sqlite3.connect(db)

    # expected values are "reports" and "restaurant"
    def get_db_from_name(self, name):
        return sqlite3.connect(name)
    
    # intialize dbs with baseline table and categories
    def initialize_dbs(self):

        reports = self.open(self.REPORTS_FILE_NAME)

        try:
            reports.execute('''CREATE TABLE REPORTS
            (ID INT PRIMARY KEY      NOT NULL,
            PLACE_ID        TEXT     NOT NULL,
            TIME            INT      NOT NULL,
            MENU_ITEM       TEXT     NOT NULL);''')

            reports.close()

            print("Reports table has been succesfully initalized.")
        except:
            print("Reports table has already been initalized.")

        restrs = self.open(self.RESTAURANTS_FILE_NAME)

        try:
            restrs.execute('''CREATE TABLE RESTAURANTS
            (ID INT PRIMARY KEY      NOT NULL,
            PLACE_ID        TEXT     NOT NULL,
            NAME            TEXT     NOT NULL,
            MENU            TEXT     NOT NULL);''')

            restrs.close()
            print("Restaurants table has been succesfully initalized.")
        except:
            print("Restaurants table has already been initalized.")

    # add a reports to the reports db
    def add_to_reports(self, place_id, time, menu_item):

        reports = self.open(self.REPORTS_FILE_NAME)
        try:
            reports.execute(f"INSERT INTO REPORTS (ID,PLACE_ID,TIME,MENU_ITEM) \
                VALUES ({self.reports_id}, \'{place_id}\', {time}, \'{menu_item}\')")
            self.reports_id += 1
        except:
            raise ValueError("something went wrong when adding a report :(")
        
        reports.commit()
        reports.close()

    # add a restaurant to the restaurants db
    def add_to_restaurants(self, place_id, name, menu):

        restrs = self.open(self.RESTAURANTS_FILE_NAME)

        try:
            restrs.execute(f"INSERT INTO RESTAURANTS (ID,PLACE_ID,NAME,MENU) \
                VALUES ({self.restr_id}, \'{place_id}\', \'{name}\', \'{menu}\')")
            self.restr_id += 1
        except:
            raise ValueError("something wrong wrong when adding a restaurant :(")
        
        restrs.commit()
        restrs.close()
    
    # returns a list of all reports relating to a place_id
    def get_reports_with_place_id(self, place_id):
        reports = self.open(self.REPORTS_FILE_NAME)

        table = reports.execute("SELECT ID, PLACE_ID, TIME, MENU_ITEM from REPORTS")
        
        # filters rows
        selected = [row for row in table if row[1]==place_id]

        reports.close()

        return selected
    
    # print reports db
    def print_reports(self):
        reports = self.open(self.REPORTS_FILE_NAME)

        table = reports.execute("SELECT ID, PLACE_ID, TIME, MENU_ITEM from REPORTS")

        for row in table:
            print (f"ID = {row[0]}")
            print (f"PLACE_ID = {row[1]}")
            print (f"TIME = {row[2]}")
            print (f"MENU_ITEM = {row[3]}")
            print("")

        reports.close()

    # print restrs db
    def print_restaurants(self):
        restrs = self.open(self.RESTAURANTS_FILE_NAME)

        table = restrs.execute("SELECT ID, PLACE_ID, NAME, MENU from RESTAURANTS")

        for row in table:
            print (f"ID = {row[0]}")
            print (f"PLACE_ID = {row[1]}")
            print (f"NAME = {row[2]}")
            print (f"MENU = {row[3]}")
            print("")

        restrs.close()

    # completely wipes the db from the dir
    def delete_dbs(self):
        os.remove(self.REPORTS_FILE_NAME)
        os.remove(self.RESTAURANTS_FILE_NAME)

        # reset ids back to 1
        self.reports_id = 1
        self.restr_id = 1