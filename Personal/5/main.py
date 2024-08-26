# importing
from geopy.geocoders import Nominatim

geoloc = Nominatim(user_agent="GetLoc")

locname = geoloc.reverse("5.5611835, 5.77331")

print(locname.address)