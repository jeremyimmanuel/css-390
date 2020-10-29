import sys
from time import sleep, time
import random
from urllib import error, request

url = sys.argv[1] 
url = 'http://' + url.lstrip('http://')
rps = int(sys.argv[2]) 
jitter = float(sys.argv[3]) 

if jitter < 0:
    jitter = 0.1
elif jitter > 1:
    jitter = 1 

a = int(rps * (1 - jitter)) 
b = int(rps * (1 + jitter))



while True:
    trueRps = random.randint(a, b)
    start = time()
    for i in range(trueRps):
        token = random.randint(0, 100)
        try:
            if token % 5 == 0:
                request.urlopen(url + '/bruh') # 404
            elif token in range(6, 29):
                request.urlopen(url + '/fail') # 500
            else:
                request.urlopen(url) # 200
        except error.HTTPError:
            continue
    end = time()

    if(1-(end-start)) > 0:
        sleep(1-(end-start))
    else:
        continue