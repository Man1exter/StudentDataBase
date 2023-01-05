import random

def menu():
    
    print(" ")
    print("[1] - ADD NEW STUDENT")
    print("[2] - DELETE STUDENT")
    print("[3] - SHOW ALL STUDENTS")
    print("[4] - EXIT QUIT CLOSE")
    print(" ")
    print(" ")
    
def stu():
    
    file = "studen.txt"
    fi = open(file, "a", encoding="utf-8")
    
    print(" ")
    print(" ")
    
    list_base = []
    
    
    names = input(" Name: ")
    surnames = input(" Surname: ")
    ages = input(" Age: ")
    classes = input(" Class: ")
    cities = input(" City: ")
    
    human = " " + names + " " + surnames + " " + ages + " " + classes + " " + cities
    
    fi.write(human + "\n")
    
    list_base.append(human)
    
    print(" ")
    
    print("NEW STUDENT ADD TO YOUR DATABASE=> ")
    
    print(" ")
    
    for x in list_base:
        print(x)
        
    fi.close()
    
def show_student():
    
    file = "studen.txt"
    fi = open(file, "r", encoding="utf-8")
    
    # SOLO LINE FROM FILE
    # print(fi.readline())
    # fi.readline()
    
    for lines in fi:
        print(lines)
    
    fi.close()
    
    

def main():
    
    #  fi = open(file,"r")
    
    # r - read, w - write, a - add new value ( dont delete ctr )
    
    #  file = "studen.txt"
    
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
           show_student()
       elif goal == "4":
           print(" ")
           print("QUIT FROM THE BASE " + log + " " + pwd)
       else:
           print(" UNKNOWN COMMAND ")
      
    else:
        print(" ")
        print("Suspicious..")
        return 0
    
main()
    