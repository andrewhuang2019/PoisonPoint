from googleplaces import GooglePlaces, types
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import os

#load and pass in API key from env file
load_dotenv()   
API_KEY = os.environ['GOOGLE_MAPS_API'] 
google_places = GooglePlaces(API_KEY)         
geolocator = Nominatim(user_agent=API_KEY)    

#sets latitude and longitude of given location 
location = geolocator.geocode("Lawrence, KS") 

#query restaurants from API within given radius of latitude and longitude 
query = google_places.nearby_search(                                
        lat_lng={'lat':location.latitude,'lng':location.longitude}, 
        radius=5000,                                                
        types=[types.TYPE_RESTAURANT])                             

#display queried restaurant names
for place in query.places:
    print(place.name)