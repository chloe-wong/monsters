simplemonsters = {}

def CreateDict():
    file = open("simplemonsters.txt", "r")
    lines = file.readlines()
    for x in lines:
        key = x.split(',')[0]
        value = x.split(',')[1]
        simplemonsters[key] = value

def Search():
    name = input("Input monster name (capitalised)")
    print("Description: ", simplemonsters[name])

def Main():
    CreateDict()
    print("Welcome to the Monster Dictionary!")
    repeat = 'T'
    while repeat == 'T':
        Search()
        repeat = input("Would you like to search again? T/F")
    print("Thank you for using the Monster Dictionary: come again soon.")


Main()
