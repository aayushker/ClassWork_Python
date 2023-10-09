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

Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),
    
pattern question
n=int(input("Enter the number of rows"))
for i in range(0, n):
    for j in range( n, 0,-1):
        print(" ", end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
    print()

To convert string to dictionary 
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
    
    
        
    