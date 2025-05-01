# Chuck Tirtasaputra
# date: October 10, 2021

# this is a ceasar ciper code that can shift the text and verifies with the user
# if the text is legible or not with multiple different text files

def caesar(text, shift):
    output = ""
    for char in text:
        newchar = ""
        char = char.lower()
        if char.isalpha() == False:
            newchar = char
        elif (shift + ord(char.lower())) > 122:
            newchar = chr(shift + ord(char.lower()) - 26)
        else:
            newchar = chr(shift + ord(char.lower()))
        output = output + newchar
    return output

def checker(text, shift):
    shifted = caesar(text, shift)
    print(shifted)
    answer = input('\nDoes the string above look like a word to you? Yes or No? ')
    if answer == "yes" or answer == "Yes":
        return True
    elif answer == "no" or answer == "No":
        return False
    else:
        answer = input('Try Again! Yes or No? ')

def decode():
    name = input("What's your name? ")
    file = input("Hi " + name + "! What's the name of the text file you want to input? ")
    textfile = file + ".txt"

    while True:
        try:
             with open(textfile, 'r+', encoding="ISO-8859-1")) as f:
                contents = f.read()
                break
        except FileNotFoundError:
            file = input("Try again! File not found! ")

    for i in range(1, 27):
        decoded = checker(contents,i)
        if decoded == True:
            decode()

decode()
