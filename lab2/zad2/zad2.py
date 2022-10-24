from datetime import datetime
import time

val = True
while(val):
    print('\r', end='')
    now = datetime.now()
    dt_string = now.strftime(chr(16) + "\t%H:%M:%S\t" + chr(17))
    print(dt_string, end='')
    time.sleep(0.5)
