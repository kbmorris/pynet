#!/usr/bin/env python3

ip_address = input("Please enter an IP address:")
for i in range(4):
    print(f"{'Octet'+str(i+1):^15}", end = '')
print()
print('-'*60)
for i in ip_address.split('.'):
    print(f"{i:^15}",end="")
print()
for i in ip_address.split('.'):
    print(f"{f'{int(i):#010b}':^15}",end="")
print()
for i in ip_address.split('.'):
    print(f"{hex(int(i)):^15}",end="")
print()
print('-'*60)