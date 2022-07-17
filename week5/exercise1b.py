# 1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' with a default value of 'cisco_ios'. Print all four of the function variables out as part of the function's execution.

def ssh_conn2(ip_addr, username, password, device_type = 'cisco_ios'):
    print(f"SSH Connection to host {ip_addr} as a {device_type} device with username: {username} and password: {password}")

# Call the 'ssh_conn2' function both with and without specifying the device_type
ssh_conn2('10.1.1.1', 'juniper', 'juniper123', 'junos')
ssh_conn2(ip_addr='10.1.2.1', password='cisco123', username='cisco')
ssh_conn2('10.2.1.1', password='arua123', username='admin', device_type='arubaos')

# Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using the **kwargs technique.
device={}
device.update({'ip_addr': '192.168.40.1'})
device.update({'username': 'admin'})
device.update({'device_type': 'unifi'})
device.update({'password': 'ubiquity123'})
ssh_conn2(**device)
