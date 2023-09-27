#22/09/2023

while (True):
    print("Which question do you want to see?")
    print("1,2,3,4")
    entry = input("Enter your choice: ")
    
    if (entry == "1"):
        a=[]
        n=int(input("How many elements do you want to enter?"))
        print("Enter the elements")
        for i in range(n):
            a.append(int(input()))
        temp = a[0]
        a[0] = a[-1]
        a[-1] = temp
        print(a)
    
    