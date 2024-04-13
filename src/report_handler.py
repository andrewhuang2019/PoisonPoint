from database_helper import DatabaseHelper

class ReportHandler:

    def __init__(self):
        self.REPORTS_FILE_NAME = "reports.db"
        self.db = DatabaseHelper()

    # The weight is our way of approximating the valid amount of reports a restaurant has
    # Essentially, older reports have less weight than newer reports, reaching zero weight at three days
    # This is because you are most likely not getting food poisoning from food you ate three days ago.
    def get_restaurant_weight(self, restr_id):
        reports_by_restr = self.db.get_reports_with_place_id(restr_id)

        sum_weights = 0
        for report in reports_by_restr:
            weight = 0
            # time elapsed is index 2 of the report
            if(report[2] <= 1):
                weight = 1
            else:
                weight = max(0, (-1/2) * report[2] + 3/2)

            sum_weights += weight
    
        return sum_weights