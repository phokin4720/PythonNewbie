num1 = int (input("จำนวนที่ 1 : ")) 
num2 = int (input("จำนวนที่ 2 : ")) 

print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 / num2)



def A () :
    num1 = int (input("number 1 : "))
    num2 = int (input("number 2 : "))
    if num1 > num2 :
        print ("มากว่า")
    elif num1 < num2 :
        print ("น้อยกว่า") 
    else :
        print ("เท่ากัน")

A()

#------------------------------------------------------------#

def Test (param1) : 
    i = 1
    while i <= param1 :
        print(i)

Test(33)

def Test (param1) : 
    for i in range(1,6) :
        print(i)

Test(33)

def Test (param1) : 
    if param1 >= 80 :
        print("A")
    else :
        print("C")  


Test(99)

#------------------------------------------------------------#

name = str(input("Enter name : ")) 
print("Hello : ",name)

#------------------------------------------------------------#

number = int(input("Enter Number 1-10 : "))
if number == 9 :
    print("Correct")
else :
    print("Not Correct!")