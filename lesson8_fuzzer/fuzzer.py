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
import datetime
import os

file_list = [
    "amazon-dynamo-sosp2007.pdf",
    "0706.1033v2.pdf",
    "1203.4740v2.pdf",
    "1207.2054v1.pdf"
]

# List of applications to test
apps = [
    ('C:/Program Files (x86)/STDU Viewer/STDUViewerApp.exe', ''),
    ("C:/Program Files/Tracker Software/PDF Editor/PDFXEdit.exe", ''),
    ("C:/Program Files/Mozilla Firefox/firefox.exe", '-p Pure -no-remote')
]

FuzzFactor = 256
num_tests = 10000

########### end configuration ##########


for i in range(num_tests):
    file_choice = random.choice(file_list)
    
    buf = bytearray(open(file_choice, 'rb').read())
    file_size = len(buf)

    # number of writes is between 1 and 1/256 of file's length
    numwrites = random.randint(1, math.ceil(file_size/FuzzFactor))

    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(file_size)
        buf[rn] = rbyte

    # building unique name for a file
    nb = os.path.basename(file_choice)
    file_name = os.path.splitext(nb)[0]
    fuzz_output = f'{file_name}_{datetime.datetime.now()}.pdf'

    open(fuzz_output, 'wb').write(buf)

    for app in apps:
        app_name = os.path.basename(app[0])
        app_args = app[1].split(' ')
        
        process = subprocess.Popen([app_name, app_args, fuzz_output])
        time.sleep(1)
        crashed = process.poll()
        if not crashed:
            process.terminate()
            # del twisted pdf from disk
            os.remove(fuzz_output)
        else:
            # log the crash
            with open('crashlog', 'a') as log:
                log.write(f'{fuzz_output} crashed {app_name} with code {crashed}\n')
