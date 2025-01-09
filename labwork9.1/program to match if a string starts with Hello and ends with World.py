import re
data = "Hello I am Namya Shah World"
q = "^Hello.*World$"
answer = re.search(q,data)
print(answer.group())