#!/usr/bin/env python3

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
fields = show_version.split()
model = fields[1]
serial = fields[2]
print('cisco' in model.lower())
print('881' in model)
print(f"Model: {model}\nSerial Number: {serial}")
