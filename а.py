f1 = open("output1.txt", "w")
with open("file.txt", "r") as myfile:
    data = myfile.read()
data_1 = data[::-1]
f1.write(data_1)
f1.close()
f2 = open("output2.txt", "w")
with open("file.txt", "r") as myfile:
    data = myfile.readlines()
data_2 = data[::-1]
f2.writelines(data_2)
f2.close()