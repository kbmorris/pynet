import re

with open('.\\week4\\show_version.txt') as f:
    output = f.read()

version = re.search(r'.*Cisco IOS Software.*Version ([^,]*).*',output).groups()[0]
serial_no = re.search(r'.*Processor board ID ([^\s]*).*',output).groups()[0]
config_reg = re.search(r'.*Configuration register is ([^\s]*).*',output).groups()[0]

print(f"OS Version: {version}")
print(f"Serial Number: {serial_no}")
print(f"Config Register: {config_reg}")