# Network Tracking Using Wireshark and Google Maps

I created a comprehensive project that capture and maps network traffic using Wireshark and Google Maps on Windows operating system. This project demonstrates my ability to work with network analysis tools, python scripting, and data visualization. This project captures network traffic using Wireshark, extracts IP addresses from the captured data, and maps their geolocations using the GeoLite2 database on Google Maps.

## Tools and Libraries

- Wireshark
- MaxMind GeoLite2
- Python (with pyshark, geoip2, and folium libraries)
- Google Maps API

## Installation

1. Install Wireshark.
2. Download the GeoLite2 City database from MaxMind and place the `GeoLite2-City.mmdb` file in the project directory.
3. Install required Python libraries:
  pip3 install pyshark geoip2 folium	

## Usage

1. Capture network traffic using Wireshark and save it as `network_traffic.pcap`.
2. Run the Python script to generate the map:
  python map_generator.py
3. Open `network_map.html` to view the network traffic on Google Maps.

## License

This project is licensed under the MIT License.
