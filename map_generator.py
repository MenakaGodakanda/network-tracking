import dpkt
import socket
import geoip2.database
import ipaddress

# Initialize the reader for the MaxMind GeoLite2 database
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

# Check for private IP
def is_private_ip(ip):
    # Check if the IP address is private
    return ipaddress.ip_address(ip).is_private

# Generate KML for IP Pair
def retKML(dstip):
    srcip = 'x.x.x.x'
    try:
        # Skip private IP addresses
        if is_private_ip(dstip):
            return ''
        
        dst = reader.city(dstip)
        src = reader.city(srcip)
        
        dstlongitude = dst.location.longitude
        dstlatitude = dst.location.latitude
        srclongitude = src.location.longitude
        srclatitude = src.location.latitude
        
        # Format KML data
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f %6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        
        return kml
    except geoip2.errors.AddressNotFoundError:
        print(f"Address not found in database: {dstip}")
        return ''
    except Exception as e:
        print(f"Error processing IP {dstip}: {e}")
        return ''

# Process PCAP File and Generate KML
def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                dst = socket.inet_ntoa(ip.dst)
                KML = retKML(dst)
                kmlPts += KML
        except Exception as e:
            print(f"Error processing packet: {e}")
            continue
    return kmlPts

def main():
    # Open the pcap file
    with open('wire.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                    '<Style id="transBluePoly">' \
                    '<LineStyle>' \
                    '<width>1.5</width>' \
                    '<color>501400E6</color>' \
                    '</LineStyle>' \
                    '</Style>'
        kmlfooter = '</Document>\n</kml>\n'
        kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
        print(kmldoc)
        
        # Save the KML data to a file
        with open('output.kml', 'w') as kmlfile:
            kmlfile.write(kmldoc)

if __name__ == '__main__':
    main()
