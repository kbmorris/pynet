#! /usr/bin/env python3

with open('.\\week2\\show_ip_bgp_summ.txt') as f:
    output = f.readlines()

bgp_local_as = output[0].split()[-1]
bgp_peer_id = output[-1].split()[0]

print(f"BGP Local AS {bgp_local_as} and Peer ID {bgp_peer_id}")
