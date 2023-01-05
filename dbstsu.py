import random

def menu():
    
    print(" ")
    print("[1] - ADD NEW STUDENT")
    print("[2] - ADD DELETE STUDENT")
    print("[3] - SHOW ALL STUDENTS")
    print("[4] - EXIT QUIT CLOSE")
    print(" ")
    print(" ")
    
def stu():
    
    print(" ")
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
    
    print("NEW STUDENT => ")
    
    print(" ")
    
    for x in list_base:
        print(x)
    

def main():
    
    log = input("LOGIN: ")
    pwd = input("PASSWORD: ")
    
    if log == "admin" and pwd == "admin" :
        
       print(" ")
       print("WELCOME " + log + " " + pwd)
       
       menu()
       
       goal = input("YOUR CHOICE: ")
       
       if goal == "1":
           stu()
       elif goal == "2":
           pass
       elif goal == "3":
           pass
       elif goal == "4":
           print(" ")
           print("QUIT FROM THE BASE " + log + " " + pwd)
       else:
           print(" UNKNOWN ")
      
    else:
        print(" ")
        print("Suspicious..")
        return 0
    
main()
    