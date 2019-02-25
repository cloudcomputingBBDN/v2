import datetime
import time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y:%S-%M-%H')
print st
