import random
name=input("What is your name?")
print("Good luck!",name)

words=['python','project','program','game']
word=random.choice(words).lower()
guesses=''
turns=12

while turns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed +=1
    if failed == 0:
        print("You win")
        print("The word is :",word)
        break

    guess=input("guess a character:")
    guesses+=guess

    if guess not in word:
        turns -=1
        print("wrong")

        print("You have",+turns,'more guesses')

        if turns==0:
            print("You loose!")
