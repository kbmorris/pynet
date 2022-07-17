# Create a dictionary representing a network device. The dictionary should 
# have key-value pairs representing the 'ip_addr', 'vendor', 'username', 
# and 'password' fields.

device = {'ip_addr': '192.168.1.1', 
            'vendor':'Juniper', 
            'username':'admin', 
            'password': 'Password'}

print(f"Device IP Address: {device['ip_addr']}")

if device['vendor'].lower() == 'cisco':
    device['platform']='ios' 
elif device['vendor'].lower() == 'juniper':
    device['platform']='junos'
elif device['vendor'].lower() == 'aruba':
    device['platform']='arubaos'
else:
    device['platform']='unknown'

bgp_fields = {'bgp_as': '65000',
                'peer_as': '65010',
                'peer_ip': '192.168.1.2'}

device.update(bgp_fields)

for item in device:
    print(f"{item}")

for (key,value) in device.items():
    print(f"{key}: {value}")
