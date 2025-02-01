#handling errors --> KeyErrors, FileNotFoundErrors, TypeError, SyntaxError, IndexError, ValueError

try:
    file = open("a_file.txt")
except FileNotFoundError: #a bare except block ignores all errors
    file = open("a_file.txt", "w")
    file.write
except KeyError as error_message: #catch the exact error
    print(f"The key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally: #a code that will run no matter what happens
    raise KeyError ("This is an error that I made") #raise is used to create our own error
    file.close()
    print("File has been closed.")

