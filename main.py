from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic



@dataclass
class Coordinates:
    latitude: float
    longitude: float


    def coordinates(self):
        return self.latitude, self.longitude
    

    
    
