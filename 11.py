from random import randrange, uniform
import time
state = 0
mv = 5
threshold = 10
spike = 0
fluctuation = 0
ispiked = 0
irested = 0
i = 1
while i != 0:
    while (mv < threshold):
        f = open("11.txt", "a")
        print ("resting")
        irested = irested + 1
        time.sleep(1)
        fluctuation = uniform(-2,5)
        mv = mv + fluctuation
        print mv
        print >> f, mv
        f.close()
    f = open("11.txt", "a")
    print("spiked!")
    print mv
    print >> f, mv
    ispiked = ispiked + 1
    time.sleep(1)
    mv = 1
    f.close()