#from random import randrange, uniform
#import time
N1mv = 0
N2mv = 0
N1mv = [line.rstrip() for line in open("11.txt")]
N2mv = [line.rstrip() for line in open("12.txt")]
i = 0
shortestlength = 0
lengthN1 = len(N1mv)
lengthN2 = len(N2mv)
threshold = 5
if lengthN1 < lengthN2:
    shortestlength = lengthN1
else:
    shortestlength = lengthN2
print N1mv
print N2mv
N1mv = map(float, N1mv)
N2mv = map(float, N2mv)
for i in range(0, shortestlength):
    if N1mv[i] > threshold and N2mv[i] > threshold:
        print ("fired together!")
        threshold = threshold - 0.5
        print threshold
    else:
        print ("did not fire together.")
        threshold = threshold + 1
        print threshold