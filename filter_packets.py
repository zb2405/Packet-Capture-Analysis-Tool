def read_write(filename, num):

    filteredfile = "Node" + str(num) + "_filtered.txt"

    with open(filename, "r") as f, open(filteredfile, "w") as file:

        for line in f:
            if "ping" in line:
                file.write(line)

def filter():

    for i in range(1,5):
        read_write(f"Node{i}.txt", i)
