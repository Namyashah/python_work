import uuid
product = []
print("E-Commerce System!")
for i in range(1,5):
    dct = {}
    order = input("Enter your product name = ")
    id = uuid.uuid4()
    dct["Name"] = order
    dct["UNIQUE_ID"] = id
    product.append(dct)
print(product)