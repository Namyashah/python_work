import uuid
id = uuid.uuid4()
print(id)
id1 = uuid.uuid5(uuid.NAMESPACE_DNS,"namya")
print(id1)