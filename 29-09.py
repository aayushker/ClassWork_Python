# List iteration
print("List iteration")
l = ["A", "B", "C"]
for i  in l:
    print(i)

# Dictionary iteration 
print("Dictionary iteration")
d=dict()
d[1]="A"
d[2]="B"
d[3]="C"
for i in d:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("This", "is", "tuple")
for i in t:
    print(i)
    
# Iterating over a String
print("\nString Iteration")
s = "WELCOME"
for i in s:
    print(i)

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),
    
# pattern question
n=int(input("Enter the number of rows"))
for i in range(0, n):
    for j in range( n, 0,-1):
        print(" ", end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
    print()

# To convert string to dictionary 
s = "WELCOME TO INDIA"
l=[]
d=dict()
l=s.split()
print(l)
d[l[0]]=l[len(l)-1]
print(d)

# prime number
n=int(input("Enter the number"))
for i in range(2, n):
    if n%i==0:
        print("Not prime")
        break
    else:
        print("Prime")
        break
    
# reversal of a number
n=int(input("Enter the number"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
``
# palindrome
n=int(input("Enter the number"))
temp=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    
    print("Palindrome")
else:
    print("Not palindrome")
    
    
# factorial
n=int(input("Enter the number"))
fact=1
for i in range(1, n+1):
    fact=fact*i
print(fact)

# fibonacci series
n=int(input("Enter the number"))
a=0
b=1
print(a)
print(b)
for i in range(2, n):
    c=a+b
    print(c)
    a=b
    b=c
    
# armstrong number
n=int(input("Enter the number"))
temp=n
sum=0
while n>0:
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if temp==sum:
    print("Armstrong")
else:
    print("Not armstrong")
    
# armstrong number in range
n=int(input("Enter the number"))
for i in range(1, n+1):
    temp=i
    sum=0
    while i>0:
        rem=i%10
        sum=sum+rem*rem*rem
        i=i//10
    if temp==sum:
        print(temp)
        
# reverse of a string
s=input("Enter the string")
l=[]
l=s.split()
print(l)
l.reverse()
print(l)
s1=" ".join(l)
print(s1)

#sorting of a list
l=[1, 5, 3, 2, 4]
l.sort()
print(l)

# sorting of a list without using sort function
l=[1, 5, 3, 2, 4]
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)



    
    
        
    