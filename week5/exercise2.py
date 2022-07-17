from random import randrange

# 2.  Create a function that randomly generates an IP address for a network. The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

# You should be able to pass a different base network into your function as an argument.
def generate_ip(network = '10.10.10.'):

# Randomly pick a number between 1 and 254 for the last octet and return the full IP address.
    host = str(randrange(1, 255))
    return network+host

# You can use the following to randomly generate the last octet:
# import random
# random.randint(1, 254)

# Call your function using no arguments.
print(generate_ip())

# Call your function using a positional argument.
print(generate_ip('1.1.1'))

# Call your function using a named argument.
print(generate_ip(network='172.16.1.'))

# For each function call print the returned IP address to the screen.
