import random

def menu():
    
    print(" ")
    print("[1] - ADD NEW STUDENT")
    print("[2] - ADD DELETE STUDENT")
    print("[3] - SHOW ALL STUDENTS")
    print(" ")
    

def main():
    
    log = input("LOGIN: ")
    pwd = input("PASSWORD: ")
    
    if log == "admin" and pwd == "admin" :
        
       print(" ")
       print("WELCOME " + log + " " + pwd)
      
       menu()
      
    else:
        print(" ")
        print("Suspicious..")
        return 0
    
main()
    