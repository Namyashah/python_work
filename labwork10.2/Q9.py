import subprocess as sub
data = [{"age":18,"number":106},{"age":12,"number":102},{"age":67,"number":103}]
answer = sorted(data,key=lambda x: x["number"])
print(answer)