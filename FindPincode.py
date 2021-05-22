# importing geopy API
from geopy.geocoders import Nominatim
geocoder = Nominatim(user_agent = 'geoapiExercise')

import pgeocode


option=float(input(" enter 1 for Pincodes \n enter 2 for longitude and latitude\n\n"))

if(option==1):
    data = pgeocode.Nominatim('In')
    pin=int(input('\nenter pin code'))
    location=(data.query_postal_code(str(pin)))
    Area=location['place_name'].split(", ")
    print(Area)
    print(location)

# below two lines are two limit the rate ,used when we are working on large data so that it doesnt give load on server
#from geopy.extra.rate_limiter import RateLimiter
#geocode = RateLimiter(geocoder.geocode, min_delay_seconds = 1,   return_value_on_exception = None)
elif(option==2):

    lat=input("\nenter latitude")
    log=input("enter longitude")

    #getting location of latitude and longitude
    location = geocoder.reverse((lat, log))
    locstr=str(location.raw)
    print( locstr.find('postcode'))
    print(location.raw)
    if( locstr.find('village')!= -1):
       print('Village: ',location.raw['address']['village'])
    if(locstr.find('suburb')>0):
       print('Suburb: ',location.raw['address']['suburb'])
    if(locstr.find('city_district')>0):
       print('Village: ',location.raw['address']['city_district'])
   #for tehsil/city
    if(locstr.find('county')>0):
        print('County: ',location.raw['address']['county'])
    if(locstr.find('city')>0):
       print('City: ',location.raw['address']['city'])
    #for district 
    if(location.raw['address']['state_district']):
        print("District:",location.raw['address']['state_district'])
    #for stateS
    print('State:',location.raw['address']['state'] )
    # getting pinCode from location
    if(locstr.find('postcode')>0):
        print('PinCode: ',location.raw['address']['postcode'])
     print('Country code: ',location.raw['address']['country_code'])