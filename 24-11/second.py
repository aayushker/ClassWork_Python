with open('output.txt', 'w') as file:
    file.write("And I am Iron Man\n")
    file.write("Anhoni Ko koi nhi taal sakta\n")
    file.write("And His name is John Cena!!")
    
with open(".\output.txt", "r") as file:
    content = file.read()
    print(content)
