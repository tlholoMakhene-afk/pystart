import sys #this allows you to use the sys.exit command to quit/logout of the application
from classes.user import User
from classes.student import student
def main():
    login()
    
def login():
 
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    newUser = User(answer1,answer2)
    if(newUser.validateUser() != False):
        print("Welcome - Access Granted")
        while True:
            menu()
    else:
         print('Invalid Creditails...')

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                     A: Enter Student details
                     B: View Student details
                     C: Search by ID number
                     D: Produce Reports
                     Q: Quit/Log Out

                    Please enter your choice: """)

    if choice == "A" or choice =="a":
            enterstudentdetails()
    elif choice == "B" or choice =="b":
            viewstudentdetails()
    elif choice == "C" or choice =="c":
            searchbyid()
    elif choice=="D" or choice=="d":
            producereports()
    elif choice=="Q" or choice=="q":
            print("Exiting....")
            sys.exit()
    else:
            print("You must only select either A,B,C, or D.")
            print("Please try again")
            menu()


#Menu methods
def enterstudentdetails():
        print("Enter New Student ID")
        enteredID=input()
        print("Enter Student Name")
        enteredName=input()
        print("Enter Student Age")
        enteredAge=input()
        InsertNewStudent(enteredID,enteredName,enteredAge)

    #Teacher will enter student details manually
    #These will be appended to the csv file

def viewstudentdetails():
   print('View All Students')
   for obj in getAllStudents(): 
    print(obj) 
#Teacher can press a button to view all students at a glance

def searchbyid():    
    #Teacher can input an ID number and display the relevant student's details
    print("Enter Student ID for view: ")
    enteredID=input()
    print('View Student with ID No:')
    print(enteredID)
    bSearch = False
    for obj in getAllStudents(): 
        if(obj.studentid == enteredID ):
            bSearch = True
            break
    if(bSearch!=False):  
          print(obj)
    else:
          print('Invalid StudentID')  
    

def producereports():
    pass
    #Teacher can produce clever reports such as:
    #a) list of names of males and email addresses
    #b) list of names of females in specific age categories
    #c) list of all names, birthdays and addresses (to send out birthday cards!)
    

    #data methods
def getAllStudents():
        #creating a list
    lstStudents = [] 
        #appending instance to list
    with open ("./New folder/students.txt", "r") as ReadingEachLine:
            lines = ReadingEachLine.readlines()
    for i in lines:
             linecontent = i.split('#')
             lstStudents.append(student(linecontent[0], linecontent[1], linecontent[2]))
             #lstStudents.append(student())
    ReadingEachLine.close()
    return lstStudents  

def InsertNewStudent(enteredID,enteredName,enteredAge):
        formattedString =  enteredID + '#' + enteredName + '#'+ enteredAge +'#'
        print('Formatted String: '+formattedString + ' --> Ready for insertion')
        f= open("./New folder/students.txt","a+")
        f.write('\n' +formattedString )
        f.close() 

#the program is initiated, so to speak, here
main()



