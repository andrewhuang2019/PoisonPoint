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
        self.issue_foods = ["Fish","Lettuce","Chicken","Beef","Eggs",
                            "Shellfish","Milk","Flour","Wasabi"]

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
    # radius is measured in meters
    def get_dangerous_ids_near_coords(self, lat, lng, radius):
        LIMIT = 10

        # get sorted ids
        ids = self.google_api.get_place_ids_in_radius_with_coords(lat, lng, radius)
        ids.sort(reverse=True, key=self.get_danger_weight)

        # limit to LIMIT
        if(len(ids) > LIMIT):
            ids = ids[:(LIMIT - 1)]
        
        return ids
    
    # wrapper for the function made in the google_places_helper.py
    # returns a dict that contains "name", "address", and "img"
    # for a map element
    def get_info_from_id(self, id):
        return self.google_api.get_info_from_place_id(id)

    # Returns a list of tuples of the most likely causes of food poisoning for a given restaurant
    # Values are sorted by the highest vals of (items_eaten) / (total_reports)
    # Returns (food_item, ratio_mentioned_above)
    def get_commonly_reported_items(self, id):
        reports_by_id = self.db.get_reports_with_place_id(id)

        total_reports = len(reports_by_id)

        # initialize a dict of zero sums (no bad reports for any item yet)
        index_to_sum_poisoned = []
        
        # traverse through each report for a given restaurant
        for report in reports_by_id:
            # get the true/false list for each report
            bool_list = self._get_bool_list_from_db_str(report[4])
            for i, food_bool in enumerate(bool_list):
                if(food_bool):
                    # keep count of each True value
                    index_to_sum_poisoned[i] += 1

        index_to_ratio = [num / total_reports for num in index_to_sum_poisoned]

        tuples_of_food_ratio = []
        for i, num in enumerate(index_to_ratio):
            food_ratio = (self.issue_foods[i], num)
            tuples_of_food_ratio.append(food_ratio)
        
        # sorts the tuples by their ratio
        sorted_tuples = tuples_of_food_ratio.sort(reverse=True, key=self._helper_sort)

        return sorted_tuples
    
    def _helper_sort(self, food_ratio_tuple):
        return food_ratio_tuple[1]
        
    # Since items_eaten is stored as a string like "True,False,False,True"
    # We need a function to turn that into an actual list of booleans
    def _get_bool_list_from_db_str(self, db_string):
        db_strings = db_string.strip().split(",")
        return [(string == "True") for string in db_strings]
    
    def add_to_db(self, place_id, days_elapsed, time, items_eaten, restaurant_name):
        self.db.add_to_reports(place_id, days_elapsed, time, items_eaten, restaurant_name)