import random
number_list = []
for i in range(0,10):
    random_number = random.randint(1,100)
    print(f"Random numbers from 1 to 100 is {random_number}")
    number_list.append(random_number)
print(number_list)