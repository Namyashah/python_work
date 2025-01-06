import uuid
main = []
for i in range(1,4):
    student = {}
    id = int(input("Enter "))
    records = uuid.uuid4()
    student["ID"] = id
    student["uuid"] = records
    main.append(student)
print(main)