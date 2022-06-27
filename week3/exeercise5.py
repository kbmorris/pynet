#! /usr/bin/env python3

import os

WINDOWS = True
IP_PREFIX = '192.168.34.'
BASE_CMD_LINUX = 'ping -c 2'
BASE_CMD_WINDOWS = 'ping -n 2'

base_cmd = BASE_CMD_WINDOWS if WINDOWS else BASE_CMD_LINUX

ip_addresses = []
for i in range(1,255):
    ip_addresses.append(f'{IP_PREFIX}{str(i)}')

for i, ip_addr in enumerate(ip_addresses):
    print(f'{i} ---> {ip_addr}')

for ip_addr in ip_addresses[2:6]:
    os.system(f"{base_cmd} {ip_addr}")


