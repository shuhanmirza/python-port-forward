import os
import time

i = 100000
while i > 0:
    i = i - 1
    logSize = os.path.getsize('error.log')
    
    print(logSize)

    if logSize > 20000:
        print("delete")
        #os.remove('error.log')
        #open('error.log', 'w')

    time.sleep(3)
