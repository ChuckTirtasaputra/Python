'''
this code starts a new text file, appends the made text file, reads the text file and rewrite the text file
'''with open ("bucketlist.txt", "w+") as f:
    f.write("1. Skydiving \n")
    f.write("2. Snowboarding \n")
    f.write("3. Skiing \n")
    f.write("4. Visit all of the countries \n")
    f.write("5. Swim \n")

with open ("bucketlist.txt", "a+") as f:
    f.write("6. Become a master of Python")
    
with open ("bucketlist.txt", "r+") as f:
    text = f.read()
    contents = text.replace("Python", "a new language")

    
with open ("bucketlist.txt", "w+") as f:
    f.write(contents)
