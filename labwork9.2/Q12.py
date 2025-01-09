import sys
import os as o
input = sys.argv
file = "".join(sys.argv[1:])
if o.path.exists(file):
    print(f"{input[1:]} Exists In File Directory!!")
else :
    print(f"{input[1:]} file does not exists in File Directory!!")
