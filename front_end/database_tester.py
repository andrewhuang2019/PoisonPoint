from database_helper import DatabaseHelper
from report_handler import ReportHandler
import time as t
import numpy as np

class DatabaseTester:
    def __init__(self):
        self.rh = None

    def test_basic_db_commands(self):
        db = DatabaseHelper()
        db.reset_dbs()
        db.initialize_dbs()
        db.add_to_reports("cfa_hq_id", 3, 1234098493, "True,False,True,False,False,False", "Chick Fil A")
        db.add_to_reports("wendys_hq_id", 2, 1235982063, "False,False,False,False,True,False", "Wendys")
        db.print_reports()
        db.reset_dbs()

    def test_recurring(self):
        db = DatabaseHelper()

    def create_random_report(self):
        self.rh = ReportHandler()
        self.rh.db.reset_dbs()
        self.rh.db.initialize_dbs()

        # get random inputs from a set list
        np.random.seed(111)
        NUM_TESTS = 100
        for i in range(NUM_TESTS):
            id = np.random.choice(['ChIJW-f1xlxvv4cRtUO6EwzWSh4', 'ChIJW-f1xlxvv4cRtUO6EwzWSh4', 'ChIJW-f1xlxvv4cRtUO6EwzWSh4',  
                        'ChIJh9mQmcVov4cRI-4Fj5L-Sno', 'ChIJOeGYLltvv4cRFQXi4Obzqpw', 'ChIJl6y18hFmv4cRoSNJ6ZOTwUs', 
                        'ChIJSwMlXVtvv4cR_tVq7XQXdUA', 'ChIJx1pLxFpvv4cR7Fdn1nhSoNE', 'ChIJF5VYEllvv4cRPBN0BLHaPnM'])
            days_since = np.random.randint(4)
            time = t.time() - ((1000) + np.random.randint(200000))

            # get a random list of True,True,False....
            bools = []
            for i in range(9):
                bools.append (np.random.choice([True,False]))
            
            # get rid of brackets
            bools = str(bools)[1:-1]

            name = self.rh.get_info_from_id(id)["name"]

            self.rh.db.add_to_reports(id, days_since, time, bools, name)

    def get_analytics_from_existing_db(self):
        id_list = self.rh.get_dangerous_ids_near_coords(38.9717, -95.2353, 5000)
        print([self.rh.get_danger_weight(id) for id in id_list])
        print(f"epicenter id: {id_list[0]}")
        print("expected: 'ChIJW-f1xlxvv4cRtUO6EwzWSh4'")

def main():
    pass
    #test_basic_db_commands()
    
    #tester = DatabaseTester()
    #tester.create_random_report()
    #tester.get_analytics_from_existing_db()

    tester = DatabaseTester()
    tester.rh = ReportHandler()
    print(tester.rh.google_api.get_info_from_place_id("ChIJW-f1xlxvv4cRtUO6EwzWSh4")["name"])
    

if __name__ == "__main__":
    main()