# importing geopy API
from geopy.geocoders import Nominatim
geocoder = Nominatim(user_agent = 'geoapiExercise')

# below two lines are two limit the rate ,used when we are working on large data so that it doesnt give load on server
#from geopy.extra.rate_limiter import RateLimiter
#geocode = RateLimiter(geocoder.geocode, min_delay_seconds = 1,   return_value_on_exception = None)

lat=input("enter latitude")
log=input("enter longitude")

#getting location of latitude and longitude
location = geocoder.reverse((lat, log))
print(location)

print(location.raw)
#for tehsil/city
print("city :",location.raw['address']['county'])
#for district 
print("District:",location.raw['address']['state_district'])
#for state
print('State:',location.raw['address']['state'] )
# getting pinCode from location
zipcode = location.raw['address']['postcode']
print('PinCode: ',zipcode)