from geopy.geocoders import Nominatim

loc = Nominatim(user_agent = 'GetLoc')

getloc = loc.geocode("60, Effurun Sapele Road Effurun")

print(getloc.address)

print("Latitude =", getloc.latitude)
print("Longitude = ", getloc.longitude)