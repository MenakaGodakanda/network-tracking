import pyshark
import geoip2.database
import folium

# Load GeoLite2 database
geoip_reader = geoip2.database.Reader('GeoLite2-City.mmdb')

# Function to get geolocation from IP address
def get_geolocation(ip):
 try:
     response = geoip_reader.city(ip)
     return {
         "latitude": response.location.latitude,
         "longitude": response.location.longitude,
         "city": response.city.name,
         "country": response.country.name
     }
 except geoip2.errors.AddressNotFoundError:
     return None

# Read the pcap file
pcap_file = 'network_traffic.pcap'
capture = pyshark.FileCapture(pcap_file)

# Extract IP addresses
ip_addresses = set()
for packet in capture:
 if 'IP' in packet:
     ip_addresses.add(packet.ip.src)
     ip_addresses.add(packet.ip.dst)

# Get geolocation data
geolocations = []
for ip in ip_addresses:
 geo_info = get_geolocation(ip)
 if geo_info:
     geolocations.append(geo_info)

# Create a map
map = folium.Map(location=[0, 0], zoom_start=2)

# Add markers to the map
for location in geolocations:
    if location['latitude'] is not None and location['longitude'] is not None:
        folium.Marker(
            [location['latitude'], location['longitude']],
            popup=f"{location['city']}, {location['country']}"
        ).add_to(map)

# Save the map to an HTML file
map.save('network_map.html')