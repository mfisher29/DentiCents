from __future__ import print_function

class Map(object):
    def __init__(self):
        self._points = []
    def add_point(self, coordinates):
        self._points.append(coordinates)
    def __str__(self):
        centerLat = sum(( x[0] for x in self._points )) / len(self._points)
        centerLon = sum(( x[1] for x in self._points )) / len(self._points)
        markersCode = "\n".join(
            [ """new google.maps.Marker({{
                position: new google.maps.LatLng({lat}, {lon}),
                map: map
                }});""".format(lat=x[0], lon=x[1]) for x in self._points
            ])
        return """
            <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>
            <div id="map-canvas" style="height: 100%; width: 100%"></div>
            <script type="text/javascript">
                var map;
                function show_map() {{
                    map = new google.maps.Map(document.getElementById("map-canvas"), {{
                        zoom: 8,
                        center: new google.maps.LatLng({centerLat}, {centerLon})
                    }});
                    {markersCode}
                }}
                google.maps.event.addDomListener(window, 'load', show_map);
            </script>
        """.format(centerLat=centerLat, centerLon=centerLon,
                   markersCode=markersCode)

'''
from googlemaps import GoogleMaps
gmaps = GoogleMaps(API_KEY)
lat, lng = gmaps.address_to_latlng("75 amherst street cambridge ma 02139")
'''

from geopy.geocoders import Nominatim
geolocator = Nominatim()
addresses=["613 Amherst St, Nashua, NH 03063",
"40 Webster St, Manchester, NH 03104",
"745 Chestnut St, Manchester, NH 03104",
"311 W River Rd, Hooksett, NH 03106",
"26 W Webster St, Manchester, NH 03104",
"57 Webster St Manchester",
"25 S Maple St, Manchester, NH 03103"
]
locations=[]
for address in addresses:
    locations.append(geolocator.geocode(address))

'''    
location1 = geolocator.geocode("75 amherst street cambridge ma 02139")
location2 = geolocator.geocode("550 memorial drive cambridge ma 02139")
'''

if __name__ == "__main__":
        map = Map()  
        for location in locations:
            map.add_point((location.latitude,location.longitude))

'''        
        map.add_point((location1.latitude, location1.longitude))
        map.add_point((location2.latitude, location2.longitude))
'''

with open("output.html", "w") as out:
    print(map, file=out)
