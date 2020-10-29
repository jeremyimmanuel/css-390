from urllib import request
import sys
import os
from time import sleep, time

# python collector.py [url] --interval [timeStep]

timeStep = 10
outputFile = 'data.tsv'

if len(sys.argv) > 2: # if flag was given
    if sys.argv[2] == '--interval':
        if len(sys.argv) > 3 and sys.argv[3].isnumeric() and sys.argv[3] > 0: #has valid input for flag
            timeStep = int(sys.argv[3])
        else:
            print('Please give appropriate time interval value (s) to flag --interval')
            sys.exit()
    else:
        print('Please use existing flag(s) for this program:\n\t--interval [desired interval]')
        sys.exit()

url = sys.argv[1]
url = 'http://' + url.lstrip('http://')
url = url.rstrip('/') + '/stats'

if os.path.isfile(outputFile): # existing file, append
    f = open(outputFile, 'a') #append
else:   # new file, write
    f = open(outputFile, 'w') #write new file 


oneHour = 3600
stop = time() + oneHour + .0001

while time() < stop:
    r = request.urlopen(url)
    valArr = r.read().decode('utf-8').split('\n')
    for val in valArr[:4]:
        v = val.split(': ')[1]
        f.write(v + '\t')
    f.write('\n')
    sleep(timeStep)