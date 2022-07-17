# 1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username, and password. The function should print out each of these three variables and clearly indicate which variable it is printing out.
def ssh_conn(ip_addr, username, password):
    print(f"SSH Connection to host {ip_addr} with username: {username} and password: {password}")

# Call this ssh_conn function using entirely positional arguments.
ssh_conn('10.1.1.1', 'cisco', 'cisco123')

# Call this ssh_conn function using entirely named arguments.
ssh_conn(ip_addr='10.1.2.1', password='cisco123', username='cisco')

# Call this ssh_conn function using a mix of positional and named arguments.
ssh_conn('10.2.1.1', password='arua123', username='admin')

