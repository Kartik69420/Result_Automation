#Author:KARTIK SHARMA
#Code Name: RESULT CALCULATOR FOR SCHOOLS
#Language:PYTHON
#Presently at:CHANDIGARH UNIVERSITY 

###########################################################
print("")
print("")
print("")
print("      @  @     @      @ @ @@@@@ @ @  @\n      @ @     @  @    @  @  @   @ @ @\n      @@     @@@@@@   @@    @   @ @@\n      @ @   @      @  @ @   @   @ @ @\n      @  @ @        @ @  @  @   @ @  @")
print("")
print("      *********************************")
print("")
print("Note: If you want to remove my digital signature, just comment off the line number 10 of source code by putting a # before print. ")
print("")
print("")

print("")

print("Welcome to the automated result calculator for schools!! It can be used to calculate results as all you have to do is enter the marks and percentage will be displayed.")

print("")
print("")

subjects = int(input("Enter the number of subjects:"))
numb = 0
marksList = []
while numb < subjects:
    numb = numb+1
# marksList = [ ]
    marks = float(input("Enter marks:\n"))
    marksList.insert(numb , marks)


Totalsum = sum(marksList)
print("Total marks gained by student are: ",Totalsum)
print("")
print("")



def percentage():
    percentage = (Totalsum/(subjects*100))*100
    return percentage
def CGPA():
    CGPA = ((Totalsum/(subjects*100))*100)/9.5
    return CGPA
print("Percentage of the student is", percentage(),"👍")
print("")
print("CGPA of the student is ", CGPA(), "👍")






    

