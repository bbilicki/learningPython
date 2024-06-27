import random
import time
import pprint


#file exceptions

f = open("sample.txt","w")
f.write('For oft, when on my couch I lie\n')
f.write('In vacant or in pensive mood\n')
f.close()

f = open("sample.txt","r")
for line in f:
    print(line,end='')
f.close()

#exception handling
try:
    f = open('sample.txt','r')
    print(f.read())
 #   f.write('boo')
except Exception as e:
    print(e)
else:
    print("File operation is successful!")
finally:
    f.close()
    print("File is closed!")

with open('sample.txt','r') as f:
    print(f.read())
 #   f.write('boo')

