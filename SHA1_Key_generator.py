import time
import hashlib
a=raw_input("Please Enter the Password:")
#print(str(a))
result = hashlib.sha1(a.encode()) 
#hexval=result.hexdigest()
hexval="cf23df2207d99a74fbe169e3eba035e633b65d94"
#print(hexval)
import re
pattern = re.compile(r'\b[0-9a-f]{40}\b')
match = re.match(pattern, hexval)
aa=match.group(0)
print(aa)
time.sleep(4)
if(match.group(0)==hexval):
	print("Valid")
#print(type(match.group(0)))
#print match.group(0)
