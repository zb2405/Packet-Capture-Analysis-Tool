def compute(ip, L, fname):
    print("called compute function in compute_metrics.py")
    return compute_metric(ip, L, fname)


def get_num(x):
    return int(''.join(num for num in x if num.isdigit()))


def compute_metric(ip, L, fname):

    reply_sent_count = reply_rcvd_count = 0
    request_sent_count = request_rcvd_count = 0
    bytes_sent = bytes_rcvd = 0
    data_sent = data_rcvd = 0

    total_time_1 = total_time_2 = 0
    count_1 = count_2 = 0
    hop_count = 0
    org_hop = 129

    # ---------- Counting metrics ----------
    for item in L:

        if item[8] == "reply":
            if item[2] == ip:
                reply_sent_count += 1
            elif item[3] == ip:
                reply_rcvd_count += 1

        if item[8] == "request":
            if item[2] == ip:
                request_sent_count += 1
                bytes_sent += int(item[5])
                data_sent += int(item[5]) - 42

            elif item[3] == ip:
                request_rcvd_count += 1
                bytes_rcvd += int(item[5])
                data_rcvd += int(item[5]) - 42

    # ---------- RTT ----------
    for i in range(len(L)-1):
        if L[i][8] == "request" and L[i][2] == ip:
            count_1 += 1
            total_time_1 += float(L[i+1][1]) - float(L[i][1])

        if L[i][8] == "request" and L[i][3] == ip:
            count_2 += 1
            total_time_2 += float(L[i+1][1]) - float(L[i][1])

    # ---------- Hop Count ----------
    for item in L:
        if item[8] == "reply" and item[3] == ip:
            hop_count += (org_hop - get_num(item[11]))

    # ---------- Final Calculations ----------
    avg_rtt = (total_time_1 / count_1) * 1000 if count_1 else 0
    request_throughput = (bytes_sent / total_time_1)/1000 if total_time_1 else 0
    request_goodput = (data_sent / total_time_1)/1000 if total_time_1 else 0
    avg_reply_delay = (total_time_2 / count_2) * 1000000 if count_2 else 0
    avg_hop = float(hop_count)/float(request_sent_count) if request_sent_count else 0

    return (
        request_sent_count,
        request_rcvd_count,
        reply_sent_count,
        reply_rcvd_count,
        round(bytes_sent,2),
        round(data_sent,2),
        round(bytes_rcvd,2),
        round(data_rcvd,2),
        round(avg_rtt,2),
        round(request_throughput,2),
        round(request_goodput,2),
        round(avg_reply_delay,2),
        round(avg_hop,2)
    )
