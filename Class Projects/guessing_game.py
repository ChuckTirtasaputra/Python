#Chuck Tirtasaputra
#PROJECT 1 (GUESSING GAME)
#September 16, 2021
'''
The code will randomly pick a number from 1 to 100 and the player will have 7 total guesses.
If they don't get it right after 7 tries, they can choose to restart or give up.
If they give up, the game will tell them the randomly picked number and the program with finish.
If they restart, the program will select another random number and the player will have another 7 guesses.
The game will keep on repeating until the player guesses correctly or until they give up. 
'''


#READ FILE
with open ("Highscores_For_Guessing_Game.txt", "r+") as f:
    line = f.readlines()
    contents = f.read()
 
    firstline = line[1:2] #LIST
    first = str(firstline) #STRING
    firstsplit = first.split() #LIST
    first_name = firstsplit[2] #1st PLACE NAME
    first = firstsplit[5] 
    first = first[:1]
    first = int(first) #1st PLACE SCORE

    secondline = line[2:3]
    second = str(secondline)
    secondsplit = second.split()
    second_name = secondsplit[2]
    second = secondsplit[5]
    second = second[:1]
    second = int(second) 
                
    thirdline = line[3:4]
    third = str(thirdline)
    thirdsplit = third.split()
    third_name = thirdsplit[2]
    third = thirdsplit[5]
    third = third[:1]
    third = int(third)

    
import sys

from random import randint
x = randint(1, 100)

guess = None
guesses = 7
tries = 1
numtries = 7
continues = 0

y = 'Yes'
u = 'yes'
n = 'No'
m = 'no'

print('You can find the highscores under "Highscores_For_Guessing_Game.txt" ')
print('You have 7 guesses and you can only type numbers, not words! If you ever want to stop, type "Quit".')


name = input('Type your name in: ')


while guess != x:

    #STARTS THE GUESSING GAME
    
    guess = input('Guess a number between 1 and 100! You have ' + str(numtries) + ' guesses left! ')
    if guess == "Quit" or guess == 'quit': #IF THEY WANT TO QUIT
        sys.exit()
              
    while guess.isdigit() != True:
        l = input('Try again! Put a number in! ')
        if l.isdigit() and int(l) <= 100 and int(l) >= 0:
            guess = int(l)
            break
    else:
        guess = int(guess)
    

    #DETERMINES TOO HIGH OR TOO LOW 
    if guess < x:
        print('Guess is too low!')
    if guess > x:
        print('Guess is too high!')

    #IF THEY GOT IT CORRECT ON THE FIRST TIME 
    if guess == x:
        print('Congrats! You guessed right!')
        if tries == 1:
            print('It took you', tries, 'guess!')
            print('You only played one time!')

            if tries < first:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write('1st Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(secondline))
                        f.write(' '.join(thirdline))
            elif tries < second:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write('2nd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(thirdline))
            elif tries < third:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write(' '.join(secondline))
                        f.write('3rd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
            
            d = input('Want to play again? TYPE YES OR NO: ')
            if d == y or d == u:
                print('The number was:', x)
                    
                from random import randint
                x = randint(1, 100)

                print("Let's play again!")
                guess != x
                guesses = 7
                numtries = 7
                tries = 1
                continues += 1
            else:
                if tries < first:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write('1st Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(secondline))
                        f.write(' '.join(thirdline))
                elif tries < second:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write('2nd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(thirdline))
                elif tries < third:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write(' '.join(secondline))
                        f.write('3rd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')

                sys.exit()

            
    #IF THEY GOT IT RIGHT AFTER MORE THAN 1 TRY 
        else:
            print('It took you', tries, 'guesses!')
            
            if tries < first:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write('1st Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(secondline))
                        f.write(' '.join(thirdline))
            elif tries < second:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write('2nd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(thirdline))
            elif tries < third:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write(' '.join(secondline))
                        f.write('3rd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        
            d = input('Want to play again? TYPE YES OR NO: ')
            if d == y or d == u:
                print('The number was:', x)
                    
                from random import randint
                x = randint(1, 100)

                print("Let's play again!")
                guess != x
                guesses = 7
                numtries = 7
                tries = 1
                continues += 1
            else:
                if tries < first:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write('1st Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(secondline))
                        f.write(' '.join(thirdline))
                elif tries < second:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write('2nd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')
                        f.write(' '.join(thirdline))
                elif tries < third:
                    with open ("Highscores_For_Guessing_Game.txt", "w+") as f:
                        f.write('HIGHSCORES\n')
                        f.write(' '.join(firstline))
                        f.write(' '.join(secondline))
                        f.write('3rd Place: ' + name + ' ' + 'scored a ' + str(tries) + '\n')

                sys.exit()
            


    #IF THEY GUESSED WRONG
    else:
        print('Try again! ')
        guesses -= 1
        tries += 1
        numtries -= 1
        
    #IF THEY RAN OUT OF GUESSES
    if guesses == 0:
        d = input('You ran out of guesses! Want to restart? ? TYPE YES OR NO! ')
        guess = x
        continues += 1

    #IF THEY DON'T WANT TO RESTART
        if d == n or d == m:
            print('You Lost!')
            print('The number was:', x)
            print('You played', continues, 'times!')
            sys.exit()

     #IF THEY WANT TO RESTART
        if d == y or d == u:
            print('The number was:', x)
             
            from random import randint
            x = randint(1, 100)

            '''print("Let's play again!")
            guess != x
            guesses = 5
            numtries = 5
            tries = 1
            continues += 1'''
            
                
    #IF PLAYER IS BEING STUPID AND PUTS A BAD INPUT
        while d != n or d != m or d != y or d != u:
            d = input('YES OR NO? ')
            
            if d == n or d == m:
                guess = x
                continues += 1
                print('You Lost!')
                print('The number was:', x)
                if continues == 1:
                    print('You played 1 time!')
                else:
                    print('You played', continues, 'times!')
                break 
                
            if d == y or d == u:
                print('The number was:', x)
                    
                from random import randint
                x = randint(1, 100)

                print("Let's play again!")
                guess != x
                guesses = 7
                numtries = 7
                tries = 1
                continues += 1
                break 
