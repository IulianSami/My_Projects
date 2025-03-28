#2.  🗺️  Create map / search location using  Python:

import folium
from geopy.geocoders import Nominatim
import webbrowser
import os

location_name = input('Enter a location:   ')

geolocator = Nominatim(user_agent='geoapi')
location = geolocator.geocode(location_name)

if location:
    # Create a map centered on user's location
    latitude = location.latitude
    longitude = location.longitude
    clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

    marker = folium.Marker([latitude, longitude], popup=location_name)
    marker.add_to(clcoding)

    # Save the map to an HTML file and open it in the default web browser
    map_file = 'location_map.html'
    clcoding.save(map_file)
    webbrowser.open('file://' + os.path.realpath(map_file))
else:
    print('Location not found. Please try again.')