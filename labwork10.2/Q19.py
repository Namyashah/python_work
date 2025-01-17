string_data = ["namya","yug","jugal","samet","shikhar","rahi","run","ha"]
def filter_data(data):
    if len(data)>3:
        return data
answer = list(filter(filter_data,string_data))
print(answer)
def upper_method(data):
    return data.upper()
answer1 = list(map(upper_method,answer))
print(answer1)
answer2 = sorted(answer1)
print(answer2)