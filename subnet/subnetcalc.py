import sys

## input file
#filename = "mskdb"
mskdb = [
    "30;4;2;255.255.255.252",
    "29;8;6;255.255.255.248",
    "28;16;14;255.255.255.240",
    "27;32;30;255.255.255.224",
    "26;64;62;255.255.255.192",
    "25;128;126;255.255.255.128",
    "24;256;254;255.255.255.0",
    "23;512;510;255.255.254.0",
    "22;1024;1022;255.255.252.0",
    "21;2048;2046;255.255.248.0",
    "20;4096;4094;255.255.240.0",
    "19;8192;8190;255.255.224.0",
    "18;16384;16382;255.255.192.0",
    "17;32768;32766;255.255.128.0",
    "16;65536;65534;255.255.0.0"
]

## constants
header = "Mask\tAddresses\tHosts\tNetmask"

# # open file - replaced by infile list
# def openfile():
#     file = open(filename, "r")
#     global lines
#     lines = file.read().split('\n')
#     file.close()

if len(sys.argv[0:]) > 1:
    action = str(sys.argv[1])
else:
    exit("No action found, quitting")

if action == "mask":
    mask = str(sys.argv[2])
    print("Subnet with mask /",mask,"\n")
    #openfile()
    for line in mskdb:
        # split each line: 0=mask, 1=addresses, 2=hosts, 3=netmask
        line = line.split(";")
        if line[0] == mask:
            print(header)
            output = "{}\t{}\t\t{}\t{}".format(line[0],line[1],line[2],line[3])
            print(output)
        else:
            continue
elif action == "addresses":
    addresses = int(sys.argv[2])
    print("Subnets with addresses equal to or greater than",addresses,"\n")
    #openfile()
    print(header)
    for line in mskdb:
        line = line.split(";")
        if int(line[1]) >= addresses:
            output = "{}\t{}\t\t{}\t{}".format(line[0],line[1],line[2],line[3])
            print(output)
        else:
            continue
elif action == "hosts":
    hosts = int(sys.argv[2])
    print("Subnets with hosts equal to or greater than",hosts,"\n")
    #openfile()
    print(header)
    for line in mskdb:
        line = line.split(";")
        if int(line[2]) >= hosts:
            output = "{}\t{}\t\t{}\t{}".format(line[0],line[1],line[2],line[3])
            print(output)
        else:
            continue
elif action == "netmask":
    netmask = str(sys.argv[2])
    print("Subnet with mask /",netmask,"\n")
    #openfile()
    for line in mskdb:
        # split each line: 0=mask, 1=addresses, 2=hosts, 3=netmask
        line = line.split(";")
        if line[3] == netmask:
            print(header)
            output = "{}\t{}\t\t{}\t{}".format(line[0],line[1],line[2],line[3])
            print(output)
        else:
            continue