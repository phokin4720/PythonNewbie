boxscore = input("enter score :")
score = int(boxscore)

if score >= 80 :
    print("A")
else :
    print("C") 


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
