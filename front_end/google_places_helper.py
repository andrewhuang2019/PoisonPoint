from googleplaces import GooglePlaces, types
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import requests
import os

class GooglePlacesHelper:
    def __init__(self):

        # hide my API key from you bastardly hungry wolves
        load_dotenv('.env')   
        API_KEY = os.environ['GOOGLE_MAPS_API'] 
        self.google_places = GooglePlaces(API_KEY)         
        self.geolocator = Nominatim(user_agent=API_KEY)    

    # returns all the place_ids of restaurants in the radius of a given lattitude and longitude
    def get_place_ids_in_radius_with_city_state(self, city_state_str, radius):
        # get the lat and lng from a "city, state_abreviation" str 
        location = self.geolocator.geocode(city_state_str) 
        lat, lng = location.latitude, location.longitude
        
        return self._get_place_ids_from_coords(lat, lng, radius)
    
    # function for a simpler case than the one given above
    def get_place_ids_in_radius_with_coords(self, lat, lng, radius):
        return self._get_place_ids_from_coords(lat,lng, radius)

    # helper function for the ones above, gets place id from lat, lng
    def _get_place_ids_from_coords(self, lat, lng, radius):
        query = self.google_places.nearby_search(
            lat_lng = {'lat':lat,'lng':lng},
            radius = radius,
            types = [types.TYPE_RESTAURANT])
        
        # return the place_id's for all the nearby restaurants 
        return [place.place_id for place in query.places]
    
    # return name, address, and photo from a given place_id
    def get_info_from_place_id(self, place_id):

        place = self.google_places.get_place(place_id=place_id)

        # evil method that magically makes more attributes of the place object appear
        place.get_details()
        
        # use Nominatim
        loc = Nominatim(user_agent="Geopy Library")

        # entering the location name
        executable_url = f"https://nominatim.openstreetmap.org/search?q={place.formatted_address}"

        response = requests.get(executable_url).json()
        print(response)

        lat = None
        lng = None

        return_dict = {"name" : place.name,
                       "address" : place.formatted_address,
                       "img" : self._get_first_image_from_place(place),
                       "id": place_id,
                       "lat" : lat,
                       "lng" : lng}
        
        return return_dict
    
    # returns the first url from a given place obj
    def _get_first_image_from_place(self, place):
        MAX_HEIGHT = 512
        MAX_WIDTH = 512

        first_photo = place.photos[0]
        # another villainous method to make more attributes appear out of nowhere
        first_photo.get(maxheight=MAX_HEIGHT, maxwidth=MAX_WIDTH)

        return first_photo.url

    # testing do not worry shh...
    def _test(self):
        ids = self.get_place_ids_in_radius_with_city_state("Lawrence, KS", 5000)
        id_0 = ids[5]
        print (self.get_info_from_place_id(id_0))

if __name__ == "__main__":
    pass
    test = GooglePlacesHelper()
    test._test()