with open("content.txt", 'r') as file:
        content = file.read()
        count = len(content.split())
        print("Number of words in the file:", count)