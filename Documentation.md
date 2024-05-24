# Project Documentation

This documentation provides a detailed steps, including setting up environment, capturing network data with Wireshark, using GeoLiteCity database for geolocation, and visualising the data on Google Maps. 

## 1. Set Up Environment

### Operating System

This project used Windows operating system environment.

### Software Tools Installation

1. **Wireshark:**
   - Open a terminal.
   - Install Wireshark by running:
     sudo apt update
     sudo apt install wireshark
   - Follow the prompts to configure Wireshark for non-root users if needed.

2. **MaxMind GeoLite2:**
   - Create an account on MaxMind's website.
   - Download the GeoLite2 City database in `.mmdb` format.

3. **Python and pip:**
   - Open a terminal.
   - Install Python and pip by running:
     sudo apt install python3 python3-pip

4. **Required Python Libraries:**
   - Open a terminal.
   - Install necessary Python libraries by running:
      pip install dpkt geoip2

# 2. Capture Network Traffic with Wireshark

1. Open Wireshark.
2. Start capturing packets on the desired network interface (e.g., `eth0`).
3. Let it run for a sufficient amount of time to capture relevant traffic.
4. Stop the capture and save the file as `wire.pcap`.

# 3. Process the PCAP File and Geolocate IPs

1. **Create a project directory:**
   - Open a terminal.
   - Create a directory for the project:
     mkdir network-tracking
     cd network-tracking

2. **Download GeoLite2 database:**
   - Place the downloaded `GeoLite2-City.mmdb` file into the `network-tracking` directory.

3. **Place the Captured Network Traffic:**
   - Place the `wire.pcap` file into the `network-tracking` directory.
  
4. **Create the Python script:**
   - Inside the `network-tracking` directory, create a file named `map_generator.py`.
   - Open `map_generator.py` in a text editor and write the python script to extract IP addresses and geolocate them.
   
# 4. Write a README.md

Inside the `network-tracking` directory, create a file named `README.md`.
