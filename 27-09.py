# 27/09/2023 

while (True):
    print("Which question do you want to see?")
    print("1,2,3,4")
    entry = input("Enter your choice: ")
    
    if (entry == "1"):
        a=int(input("Enter the element"))
        b=int(input("Enter the element"))
        while True :
            op=input("Enter the operator or 0 to end")
            if (op=='+'):
                print("Sum=",a+b)
            elif( op=='-'):
                print("Sub=",a-b)
            elif (op=='*'):
                print("Multiplication=",a*b)
            elif (op=='/'):
                print("Multiplication=",a/b)
            elif (op=='0'):
                print("End")
                break
            
    elif (entry == "2"):   
        a= input("Enter the character")
        if (a>="A" and a<="Z"):
            print("Upper case")
        elif (a>="a" and a<="z"):
            print("Lower Case")
        else:
            print("Error")
            
    elif (entry == "3"):
        a= int(input("Enter first number"))
        b= int(input("Enter second number"))
        c= int(input("Enter third number"))
        if (a>b and a>c):
            print("Greatest is",a)
        elif (b>a and b>c):
            print("Greatest is:",b)
        elif (c>a and c>b):
            print("Greatest is:",c)

    elif (entry == "4"):
        a= int(input("Enter the number"))
        b=a/10
        if (b%5==0):
            print("Divisible by 5")
        else:
            print("Not divisible by 5")
    
    elif (entry == "0"):
        print("End")
        break
    
    else:
        print("Invalid entry")
        print("Please enter a valid entry or press 0 to end")
        continue
    
        
        