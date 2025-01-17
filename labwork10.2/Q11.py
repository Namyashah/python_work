string = ["1","2","3","4","5"]
def string_number(convert):
    return int(convert)

answer = list(map(string_number,string))
print(answer)