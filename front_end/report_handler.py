from database_helper import DatabaseHelper
import time

class ReportHandler:

    def __init__(self):
        self.REPORTS_FILE_NAME = "reports.db"
        self.db = DatabaseHelper()

    # The weight is our way of approximating the valid amount of reports a restaurant has
    # Essentially, older reports have less weight than newer reports, reaching zero weight at three days
    # This is because you are most likely not getting food poisoning from food you ate three days ago.
    def get_restaurant_weight(self, restr_id):
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