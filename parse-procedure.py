data = open("E:/Cyber/LUKPreprocess/lurkparse2.txt").readlines()
for n,line in enumerate(data):
    if line.startswith("Frame"):
       data[n] = "\n"+line.rstrip()
    else:
       data[n]=line.rstrip()
final = '|'.join(data)
with open('E:/Cyber/LUKPreprocess/lurkparse3.txt', 'w') as f:
    f.writelines(final)


def shark(s):
    import pyshark
    cap = pyshark.FileCapture('E:/Cyber/test.pcap')
    print(cap[s])

def pcapinfo():
    import sys
    from pcapfile import savefile
    testcap = open('E:/Cyber/test.pcap', 'rb')
    capfile = savefile.load_savefile(testcap, verbose=True)
    sys.stdout = open('E:/Cyber/pcapinfo.txt', 'w')
    print capfile


def find():
    import re
    from operator import sub
    cap = open('E:/Cyber/pcapinfo.txt')
    linesCounter = 1
    for line in cap:
        if linesCounter == 5:
           search = [x -1 for x in map(int, re.findall(r'[\d]+', line))]
           print search[0]
        linesCounter += 1
    for i in range(search[0]):
        print i
        shark(i)


find()
