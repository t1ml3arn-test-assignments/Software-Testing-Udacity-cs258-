# 5-line fuzzer below is from Charlie Miller's
# "Babysitting an Army of Monkeys":
# Part 1 - http://www.youtube.com/watch?v=Xnwodi2CBws
# Part 2 - http://www.youtube.com/watch?v=lK5fgCvS2N

# List of files to use as initial seed
import time
import subprocess
import string
import random
import math
file_list = [
    "amazon-dynamo-sosp2007.pdf",
    "0706.1033v2.pdf",
    "1203.4740v2.pdf",
    "1207.2054v1.pdf"
]

# List of applications to test
apps = [
    "/Applications/Adobe Reader.app/Contents/MacOS/AdobeReader",
    "/Applications/PDF Nomad.app/Contents/MacOS/PDF Nomad"
]

fuzz_output = "fuzz.pdf"


FuzzFactor = 250
num_tests = 10000

########### end configuration ##########


for i in range(num_tests):
    file_choice = random.choice(file_list)
    app = random.choice(apps)

    buf = bytearray(open(file_choice, 'rb').read())

    # start Charlie Miller code
    numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1

    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c" % (rbyte)
    # end Charlie Miller code

    open(fuzz_output, 'wb').write(buf)

    process = subprocess.Popen([app, fuzz_output])

    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()
