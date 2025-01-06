import uuid
id1 = uuid.uuid4()
print(id1)
id2 = uuid.uuid4()
print(id2)
if id1==id2:
    print("Both uuid are same")
else:
    print("Both are not same")