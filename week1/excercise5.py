#!/usr/bin/env python3

# Arp entries from exercise
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# Put arp entries into a list
arp_output = [mac1, mac2, mac3]

# Make a dictionary for each entry
arp_table = []
for arp_entry in arp_output:
    address_type, ip_address, age, mac_address, encapsulation, interface = arp_entry.split()
    arp_table.append({'AddressType': address_type, 'IPAddress': ip_address, 'Age': age, 'MACAddress': mac_address, 'Encapsulation': encapsulation, 'Interface': interface})

# Print Table
print(f"{'IP ADDR':>20} {'MAC ADDRESS':>20}")
print(f"{'-'*20} {'-'*20}")
for entry in arp_table:
    print(f"{entry['IPAddress']:>20} {entry['MACAddress']:>20}")