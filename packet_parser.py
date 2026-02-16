def parse(file_name, L):
    print("called parse function in packet_parser.py")
    file_parsing(file_name, L)

def file_parsing(fname, L):

    with open(fname, "r") as f:
        for line in f:
            L.append(line.strip().split())
