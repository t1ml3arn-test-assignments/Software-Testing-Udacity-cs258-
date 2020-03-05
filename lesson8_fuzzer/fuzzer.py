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
    "pdfs_to_test/BasicElectronics.pdf",
    "pdfs_to_test/Seeing in 3-D With Just One Eye.pdf",
    "pdfs_to_test/0706.1033v2.pdf",
    "pdfs_to_test/1207.2054v1.pdf"
]

# List of applications to test
apps = [
    ('C:/Program Files (x86)/STDU Viewer/STDUViewerApp.exe', ''),
    ("C:/Program Files/Tracker Software/PDF Editor/PDFXEdit.exe", ''),
    ("C:/Program Files/Mozilla Firefox/firefox.exe", '')
]

FuzzFactor = 150
fuzz_file_name = './fuzz.pdf'

########### end configuration ##########

def run_tests(num_tests):

    for filepath in file_list:
        print(f'fuzzing {filepath} {num_tests} times...\n')
        
        for i in range(num_tests):
            
            buf = None

            with open(filepath, 'rb') as source_file:
                buf = bytearray(source_file.read())

            file_size = len(buf)

            # number of writes is between 1 and 1/FuzzFactor of file's length
            numwrites = random.randint(1, math.ceil(file_size/FuzzFactor))

            for j in range(numwrites):
                rbyte = random.randrange(256)
                rn = random.randrange(file_size)
                buf[rn] = rbyte

            with open(fuzz_file_name, 'wb') as fuzfile:
                fuzfile.write(buf)

            print(f'Test run № {i+1}: {numwrites} bytes written into {file_size} bytes buffer')
            for app in apps:
                app_path = app[0]
                app_name = os.path.basename(app_path)
                app_args = app[1].split(' ')
                
                process_args = [app_path] + app_args + [fuzz_file_name]
                process = subprocess.Popen(process_args, shell=True)
                
                if 'firefox' in app_name:
                    time.sleep(2)
                else:
                    time.sleep(1)
                
                returncode = process.poll()
                # if not returncode:
                if returncode is None or returncode == 0:
                    os.system(f'taskkill /f /im {app_name} /t')
                else:
                    # building unique name for a filedump
                    nb = os.path.basename(filepath)
                    file_name = os.path.splitext(nb)[0]
                    timestamp = str(datetime.datetime.now()).replace(':', '-')
                    fuzz_output = f'{file_name}_{timestamp}.pdf'
                    
                    # save the file
                    with open(fuzz_output, 'wb') as out:
                        out.write(buf)
                    
                    # log the crash
                    with open('crashlog.txt', 'a') as log:
                        log.write(f'{fuzz_output} crashed {app_name} with code {returncode}. There were {numwrites} bytes written into a file.\n')
                    
        print(f'Fuzzing of {filepath} is done\n')

numtests = input('Enter number of test trials: ')

try:
    numtests = int(numtests)
except:
    numtests = 10000

run_tests(numtests)