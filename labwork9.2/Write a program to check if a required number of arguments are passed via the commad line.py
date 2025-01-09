import sys
input = sys.argv
data = "".join(input)
if input==[]:
    print("Not Enough Arguments!!")
else :
    print(f"Assigined Arguments : {input[1:]}")