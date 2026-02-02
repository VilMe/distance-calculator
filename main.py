from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic



@dataclass
class Coordinates:
    latitude: float
    longitude: float


    def coordinates(self):
        return self.latitude, self.longitude
    

def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user.agent='distance_calculator')
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)