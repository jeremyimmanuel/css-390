# Scripting-Language-Website-Monitoring

Jeremy Tandjung
Website Monitoring
CSS 390 - Scripting Language
Prof. Morris Bernstein

## Assignment Link

[Here](http://courses.washington.edu/css390/scripting/2019-q4/assignment-04.html)

## Instructions
1. Run server file (python2)
```bash
python2 timeserver.py
```
2. run traffic generator file (python3)
```bash
python3 trafficgen.py [url] [rps] [jitter]
```
3. run collector file (python3)
```bash
python3 collector.py --interval [time interval in seconds]
```
4. run plot file (python3)
```
python3 plot.py --delta_t [time step value]
```

All flags are optional

plot.py should delete the input file after running. I had multiple copies of data.tsv because I wanted to test plot.py
