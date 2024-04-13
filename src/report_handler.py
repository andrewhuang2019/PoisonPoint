from database_helper import DatabaseHelper
from google_places_helper import GooglePlacesHelper
import time

'''
The report handler class is the toplevel functionality for most of the backend
It has the database as well as the google api helper

'''

class ReportHandler:

    def __init__(self):
        self.REPORTS_FILE_NAME = "reports.db"
        self.db = DatabaseHelper()
        self.google_api = GooglePlacesHelper()
        
        # holds the list of foods that are prone to give food poisoning
        # fish, lettuce, chicken, beef, etc..
        issue_foods = []
        self.index_to_food = {}
        for i, food in enumerate(issue_foods):
            self.index_to_food[i] = food

    # The weight is our way of approximating the valid amount of reports a restaurant has
    # Essentially, older reports have less weight than newer reports, reaching zero weight at three days
    # This is because you are most likely not getting food poisoning from food you ate three days ago.
    def get_danger_weight(self, restr_id):
        reports_by_restr = self.db.get_reports_with_place_id(restr_id)

        curr_time = int(time.time())

        sum_weights = 0
        for report in reports_by_restr:
            weight = 0
            
            # this part is meant to exclude reports of you eating food a long time ago, so it cannot get you sick
            # time elapsed is index 2 of the report
            if(report[2] <= 1):
                weight = 1
            else:
                weight = max(0, (-1/2) * report[2] + 3/2)

            # this part is meant to prioritize recent reports, and ignore ones from 3+ days ago
            weight_mult = 1
            SECS_IN_DAY = 86400
            DAY_DECAY = 3
            days_since_report = (curr_time - report[3]) / SECS_IN_DAY
            weight_mult = max(0, (-1 / DAY_DECAY) * days_since_report + 1)

            weight = weight * weight_mult

            sum_weights += weight
    
        return sum_weights
    
    # Returns a list of place_ids inside of a given radius and lat,lng coordinate
    # the list is also sorted by the weighted danger sum
    def get_dangerous_ids_near_coords(self, lat, lng, radius):
        LIMIT = 10

        # get sorted ids
        ids = self.google_api.get_place_ids_in_radius_with_coords(lat, lng, radius)
        ids.sort(reverse=True, key=self.get_danger_weight())

        # limit to LIMIT
        if(len(ids) > LIMIT):
            ids = ids[:(LIMIT - 1)]
        
        return ids
    
    # wrapper for the function made in the google_places_helper.py
    # returns a dict that contains "name", "address", and "img"
    # for a map element
    def get_info_from_id(self, id):
        self.google_api.get_info_from_place_id(self, id)

    # Returns a list of the most likely causes of food poisoning for a given restaurant
    # It returns a list of the highest vals of (items_eaten) / (total_reports)
    def get_commonly_reported_items(self, id):
        reports_by_id = self.db.get_reports_with_place_id(id)

        total_reports = len(reports_by_id)

    # Since items_eaten is stored as a string like "True,False,False,True"
    # We need a function to turn that into an actual list of booleans
    def get_bool_list_from_db_str(self, string):
        to_return = []
