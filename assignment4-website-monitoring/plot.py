import matplotlib.pyplot as plt 
import sys
from datetime import datetime
import os

filename = sys.argv[1]

timeArr, arr200, arr404, arr500 = [], [], [], []

# getData
with open(filename, 'r') as tsvFile:
    for line in tsvFile:
        lineArr = line.split()
        timeArr.append(int(lineArr[0]))
        arr500.append(int(lineArr[1]))
        arr200.append(int(lineArr[2]))
        arr404.append(int(lineArr[3]))


os.remove(filename)

samplingRate = timeArr[1] - timeArr[0] 
dt = 60 

# python ploy.py [tsvFile] --delta_t [dtValue]

if len(sys.argv) > 2:
    if sys.argv[2] == '--delta_t':
        if len(sys.argv) > 3 and sys.argv[3].isnumeric() and int(sys.argv[3]) > 0: #given value
            newDt = int(sys.argv[3])
            if newDt  % samplingRate == 0: #if newDt is a discrete multiple of samplingRate
                dt = newDt
            else: 
                print('Please enter discrete multplication of %d.' % samplingRate)
                sys.exit()
        else:
            print('Please enter new delta T value after flag --delta_T (seconds)')
            sys.exit()
    else: 
        print('Unknown flag "%s"' % sys.argv[2])
        sys.exit()

step = dt // samplingRate # 60 / 10





def getDiff(target: list, source: list, i: int, diff: int, dt: int):
    target.append(source[i] - source[i - diff])


darr200, darr404, darr500, dtimeArr = [], [], [], []

for i in range(step, len(arr200), step):
    getDiff(darr200, arr200, i, step, dt) 
    getDiff(darr404, arr404, i, step, dt) 
    getDiff(darr500, arr500, i, step, dt)
    dtimeArr.append(timeArr[i]) 



for i in range(len(dtimeArr)):
    date = datetime.fromtimestamp((dtimeArr[i]))
    val = '%d:%d' % (date.hour, date.minute)
    dtimeArr[i] = val

fig = plt.figure()
plt.plot(dtimeArr, darr200, label = '200s')
plt.plot(dtimeArr, darr404, label = '404s')
plt.plot(dtimeArr, darr500, label = '500s')
plt.ylabel('RPS(%d minute-rate)' % (dt // 60))
plt.xlabel('Time')
plt.legend()
plt.title('Time server request rate over time\n(with a one-hour sample)')

fig.savefig('result.jpg')
plt.show()