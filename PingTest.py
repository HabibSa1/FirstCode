import subprocess
import os

myfile = open ("C:/Users/thinkpad/Desktop/python_Projects/myCv.txt",'w')

#myfile = open ("myCv.txt",'w')

for n in range (1, 10):
    ip = "192.168.1.{0}".format(n)
    results = subprocess.call(["ping", ip], stdout=myfile, stderr=myfile)
    if results == True:
        print(ip, results)
    else :
        print(ip, results)
