# Network Tracking Using Wireshark and Google Maps

I created a comprehensive project that capture and maps network traffic using Wireshark and Google Maps on Windows operating system. This project demonstrates my ability to work with network analysis tools, python scripting, and data visualization. This project captures network traffic using Wireshark, extracts IP addresses from the captured data, and maps their geolocations using the GeoLite2-City database on Google Maps.

## Tools and Libraries

- Wireshark
- Python
  - Python 3.x
  - dpkt
  - geoip2
  - ipaddress
- MaxMind GeoLite2-City.mmdb database
- Google Maps

## Installation

1. Install Wireshark.
2. Download the GeoLite2 City database from MaxMind and place the `GeoLite2-City.mmdb` file in the project directory.
3. Install required Python libraries:<br>
  pip install dpkt geoip2	

## Usage

1. Capture network traffic using Wireshark and save it as `wire.pcap`.
2. Place the `map_generator.py`, `wire.pcap`, `GeoLite2-City.mmdb` files into a same directory.
3. Replace source IP address in the `map_generator.py` with your public IP address. You can find the public IP address of your computer by visiting one of these websites: (<a href="https://www.whatsmyip.org/">whatsmyip.org</a>  <a href="https://www.whatismyip.com/">whatismyip.com</a>): <br>
srcip = 'x.x.x.x'
4. Run the Python script to generate the `output.kml` file: <br>
  python map_generator.py
3. `map_generator.py` will create `output.kml` and verify it for valid placemark entries.
4. Open <a href="https://www.google.com/maps/d/">Google My Maps</a> and upload `output.kml` to view the network traffic on Google Maps.

![1](https://github.com/MenakaGodakanda/network-tracking/assets/156875412/36fafb9b-c0ff-4f02-b759-4ceb12b4ae13)
![2](https://github.com/MenakaGodakanda/network-tracking/assets/156875412/b5912222-bc82-4f85-a26e-91090e3f1548)
![3](https://github.com/MenakaGodakanda/network-tracking/assets/156875412/48e82f59-5cba-40d2-88f7-3ee167c0e0ca)
![4](https://github.com/MenakaGodakanda/network-tracking/assets/156875412/36535e1e-e122-43ab-94d5-dce05b3c4f68)
![5](https://github.com/MenakaGodakanda/network-tracking/assets/156875412/b0fdb495-d2e0-473f-8ca1-29caf27b88fb)

## License

This project is licensed under the MIT License.
