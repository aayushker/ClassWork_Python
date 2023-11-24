with open("output.txt",'w') as f:
	f.write("this is my first file handling program in python\n")

with open("output.txt",'r') as f:
    print(f.read())