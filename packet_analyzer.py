#!/usr/bin/python

from filter_packets import *
from packet_parser import *
from compute_metrics import *

# Lists for parsed packets
nodes_data = {
    "Node1": ("192.168.100.1", [], "Node1_filtered.txt"),
    "Node2": ("192.168.100.2", [], "Node2_filtered.txt"),
    "Node3": ("192.168.200.1", [], "Node3_filtered.txt"),
    "Node4": ("192.168.200.2", [], "Node4_filtered.txt"),
}

output_file = "miniproject2_output.csv"

# Step 1: Filter packets
filter()

# Step 2: Parse packets
for node in nodes_data:
    ip, L, fname = nodes_data[node]
    parse(fname, L)

# Step 3: Compute and write results
newline = "\n"

with open(output_file, "w") as file:

    for node in nodes_data:
        ip, L, fname = nodes_data[node]

        (a,b,c,d,e,f,g,h,i,j,k,l,m) = compute(ip, L, fname)

        file.write(node + newline)
        file.write("Echo Requests Sent,Echo Requests Recieved,Echo Replies Sent,Echo Replies Recieved" + newline)
        file.write(f"{a},{b},{c},{d}" + newline)

        file.write("Echo Request Bytes sent (bytes),Echo Request Data Sent (bytes)" + newline)
        file.write(f"{e},{f}" + newline)

        file.write("Echo Request Bytes Recieved (bytes),Echo Request Data Recieved (bytes)" + newline)
        file.write(f"{g},{h}" + newline)

        file.write(newline)
        file.write(f"Average RTT (miliseconds),{i}" + newline)
        file.write(f"Echo Request Throughput (kB/sec),{j}" + newline)
        file.write(f"Echo Request Goodput (kB/sec),{k}" + newline)
        file.write(f"Average Reply Delay (microseconds),{l}" + newline)
        file.write(f"Average Echo Request Hop Count,{m}" + newline)
        file.write(newline)
