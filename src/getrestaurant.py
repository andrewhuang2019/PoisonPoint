from googleplaces import GooglePlaces, types
from dotenv import load_dotenv
import os

#load and pass in API key from env file
load_dotenv()
API_KEY = os.environ['GOOGLE_MAPS_API']
google_places = GooglePlaces(API_KEY)

#query restaurants from API within given radius of latitude and longitude 
query = google_places.nearby_search(
        lat_lng={'lat': 38.973148, 'lng': -95.238251}, 
        radius=5000,
        types=[types.TYPE_RESTAURANT])

#display queried restaurant names
for place in query.places:
    print(place.name)