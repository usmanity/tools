# This program displays how many days are left in the year
# and how many miles I need to ride per day until December 25th
# to get to 1,000 miles

# setting up environment
import os
import datetime
import math
import requests
from dotenv import load_dotenv

load_dotenv()
strava_api_key = os.getenv('strava_api_key')
my_user_id = 245104
strava_url = f"https://www.strava.com/api/v3/athletes/{my_user_id}/stats?access_token={strava_api_key}"

miles_per_meter = 0.000621371
realism_multiplier = 0.75
goal_miles = 1000

#  days left in the year
now = datetime.datetime.today()
end_of_year = datetime.datetime(now.year, 12, 25) # purposely not end of year
diff = end_of_year - now
days_until_xmas = diff.days

# effective meanly I mostly ride on weekend, excluding weekends except once in awhile weekend rides
effective_days = math.floor(days_until_xmas * realism_multiplier)

# total miles I have
api_call = requests.get(strava_url)
response_json = api_call.json()

meters_ytd_total = response_json['ytd_ride_totals']['distance']
miles_this_year = math.floor(miles_per_meter * meters_ytd_total)
# miles_this_year = 369

# miles per day needed, rounded up to 10th of a mile
miles_needed_per_day = round((float(goal_miles) - float(miles_this_year)) / float(effective_days), 1)

# print everything below here
print(f"Days until Christmas 🎄 : {days_until_xmas} days")
print(f"Effective days left: {effective_days} days")
print(f"Miles so far: ~ {miles_this_year} miles")
print(f"Miles needed to ride everyday: {miles_needed_per_day} miles per days")
