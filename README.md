# Packet Capture Analysis Tool (PCA)

## Overview

This project implements a **Packet Capture Analysis (PCA)** tool written
in Python. The tool analyzes ICMP packet capture data collected from
multiple network nodes and computes performance and network metrics used
for analysis.

This project was completed as part of **NSSA-220 Mini Project 2**.

------------------------------------------------------------------------

## Project Objective

The goal of this project is to:

-   Filter ICMP Echo Request and Reply packets
-   Parse packet fields from raw capture files
-   Compute network performance metrics per node
-   Export results into a CSV report

The tool calculates 13 different metrics including RTT, throughput,
goodput, reply delay, and hop count.

------------------------------------------------------------------------

## How the Tool Works

### Phase 1 --- Packet Filtering

Reads raw Node\*.txt packet capture files and filters only ICMP packets.

Output files:

Node1_filtered.txt\
Node2_filtered.txt\
Node3_filtered.txt\
Node4_filtered.txt

------------------------------------------------------------------------

### Phase 2 --- Packet Parsing

Filtered packets are parsed into structured lists containing:

-   Timestamp
-   Source IP
-   Destination IP
-   Packet Length
-   TTL
-   Request/Reply Type

------------------------------------------------------------------------

### Phase 3 --- Metric Computation

The tool computes:

Data Size Metrics - Echo Requests Sent / Received - Echo Replies Sent /
Received - Request Bytes and Data Sent/Received

Time-Based Metrics - Average RTT (ms) - Throughput (kB/sec) - Goodput
(kB/sec) - Average Reply Delay (µs)

Distance Metric - Average Hop Count

All results are exported to:

miniproject2_output.csv

------------------------------------------------------------------------

## Project Structure
```


    .
    ├── packet_analyzer.py
    ├── filter_packets.py
    ├── packet_parser.py
    ├── compute_metrics.py
    ├── Node1.txt
    ├── Node2.txt
    ├── Node3.txt
    ├── Node4.txt
    └── miniproject2_output.csv
```

------------------------------------------------------------------------

## Requirements

-   Python 3.x
-   Packet capture text files (Node\*.txt)

No external Python libraries are required.

------------------------------------------------------------------------

## How to Run

Run the main analyzer:

``` bash
python packet_analyzer.py
```

The script will:

1.  Filter packets
2.  Parse filtered data
3.  Compute metrics
4.  Generate CSV output

------------------------------------------------------------------------

## Learning Outcomes

-   Packet capture analysis
-   ICMP protocol understanding
-   RTT and throughput calculations
-   Modular Python programming
-   File parsing and reporting

------------------------------------------------------------------------

## Author

Zaki Bawade\
NSSA-220 Packet Capture Analysis Tool
