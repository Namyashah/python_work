def file():
    file = open("sample.txt","w")
    return file.write("I am fine")
    file.close()
