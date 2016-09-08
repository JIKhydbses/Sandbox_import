name = input("Please enter your name : ")
print("Every second letter of the name " + name + " is ", end="")

for i in range(len(name)):
    if i % 2 == 1:
        print(name[i] + " ", end="")
