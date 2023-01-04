def stu():
    print(" ")
    
    list_base = []
    
    names = input("Name: ")
    surnames = input("Surname: ")
    ages = input("Age: ")
    classes = input("Class: ")
    cities = input("City: ")
    
    human = names + " " + surnames + " " + ages + " " + classes + " " + cities
    
    
    list_base.append(human)
    
    print(" ")
    
    for x in list_base:
        print(x)

stu()