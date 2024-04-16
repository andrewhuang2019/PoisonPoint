import sqlite3
import os

'''
        The report database has:
            - an ID, used for something in SQLite (idk)
            - A google place ID of the parent restaurant it was made for
            - The days passed since the report was made (integer)
            - Time in seconds since 1/1/1970
            - An X length list "[True,False,True...]" casted to a string representing what
                categories of food an individual consumed during a single visit
            - Name of restaurant 
'''

class DatabaseHelper:
    
    def __init__(self):
        self.REPORTS_FILE_NAME = "reports.db"

        num = 0

        # initialize db if it does not exist
        try:
            num = self.get_all_reports().arraysize + 1
        except:
            self.initialize_dbs()

        self.reports_id = num + 1

    def open(self):
        return sqlite3.connect(self.REPORTS_FILE_NAME)
    
    # intialize dbs with baseline table and categories
    def initialize_dbs(self):

        reports = self.open()

        try:
            self.reports_id = 1
            reports.execute('''CREATE TABLE REPORTS
            (ID INT PRIMARY KEY      NOT NULL,
            PLACE_ID        TEXT     NOT NULL,
            DAYS_ELAPSED    INT      NOT NULL,
            TIME            INT      NOT NULL,
            ITEMS_EATEN     TEXT     NOT NULL,
            RESTAURANT_NAME TEXT     NOT NULL);''')

            reports.close()

            #print("Reports table has been succesfully initalized.")
        except:
            pass
            #print("Reports table has already been initalized.")

    # add a reports to the reports db
    def add_to_reports(self, place_id, days_elapsed, time, items_eaten, restaurant_name):

        reports = self.open()
    
        reports.execute(f"INSERT INTO REPORTS (ID,PLACE_ID,DAYS_ELAPSED,TIME,ITEMS_EATEN,RESTAURANT_NAME) \
            VALUES ({self.reports_id}, \'{place_id}\',{days_elapsed}, {time}, \'{items_eaten}\', \'{restaurant_name}\')")
        print(self.reports_id)
        self.reports_id += 1
        
        reports.commit()
        reports.close()
    
    # gets all pieces of data from the database
    def get_all_reports(self):

        reports = self.open()
        table = reports.execute("SELECT ID, PLACE_ID, DAYS_ELAPSED, TIME, ITEMS_EATEN, RESTAURANT_NAME from REPORTS")
        reports.close()
        return table

    # returns a list of all reports relating to a place_id
    def get_reports_with_place_id(self, place_id):
              
        reports = self.open()
        # filters rows
        table = reports.execute("SELECT ID, PLACE_ID, DAYS_ELAPSED, TIME, ITEMS_EATEN, RESTAURANT_NAME from REPORTS")
        selected = [row for row in table if row[1]==place_id]

        reports.close()
        return selected
    
    # print reports db
    def print_reports(self):
        reports = self.open()

        table = reports.execute("SELECT ID, PLACE_ID, DAYS_ELAPSED, TIME, ITEMS_EATEN, RESTAURANT_NAME from REPORTS")
        for row in table:
            print (f"ID = {row[0]}")
            print (f"PLACE_ID = {row[1]}")
            print (f"DAYS_ELAPSED = {row[2]}")
            print (f"TIME = {row[3]}")
            print (f"ITEMS_EATEN = {row[4]}")
            print (f"RESTAURANT_NAME = {row[5]}")
            print("")

        reports.close()

    # completely wipes the db from the dir
    def reset_dbs(self):
        if(os.path.exists(self.REPORTS_FILE_NAME)):
            os.remove(self.REPORTS_FILE_NAME)

        # reset ids back to 1
        self.reports_id = 1