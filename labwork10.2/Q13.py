string = ["namya","yug","jugal","rahi","adish"]
def short(st):
    if len(st)<=4:
        return st

answer = list(filter(short,string))
print(answer)