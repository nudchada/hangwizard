import random

# List of Harry Potter Characters
from characters import characters

def main():
    print("How to play HangWizard:\n\
1. The secret word is the characters from Harry Potter, including wizards, witches, muggles, and non-humans.\n\
2. You can guess only one letter each time (uppercase or lowercase).\n\
3. If the letter is in the secret name, it will appear in the blank.\n\
4. If the letter isn't in the secret name, a new body part is added to the hangWizard.\n\
5. You have 8 chances to guess wrong.  When you have no chance game is over.\n\
6. When you get the secret name, you win.")

    secret=random.choice(characters).upper()
    word=[]
    for c in secret:
        if c.isalpha():
            word.append('_')
        else:
            word.append(c)
    print(' '.join(word))
    chances=8
    while chances>0:
        letter=guessing()
        if letter in secret:
            word=fill_blank(secret,word,letter)
            print(' '.join(word))
            if ''.join(word)==secret:
                print ("You Win!")
                print('The secret name is ' + secret)
                break
        else:
            chances-=1
            print("chances: " + str(chances))
            print(hangWizard(chances))
            print(' '.join(word))
            if chances==0:
                print('GAME OVER!')
                print('The secret name is ' + secret)

# get input from user
def guessing():
    while True:
        letter=input('Please enter one letter: ')
        if len(letter)==1 and letter.isalpha():
            return letter.upper()
        else:
            continue

# fill blank when get correct letter
def fill_blank(secret,word,letter):
    for i in range(len(secret)):
        if secret[i]==letter:
            word[i]=letter
    return word

# create hangman
def hangWizard(chances):
    step = [" _____\n|\n|\n|\n|\n|_____",
    " _____\n|\n|  O  \n|\n|\n|_____",
    " _____\n|\n|  O  \n|  |  \n|\n|_____",
    " _____\n|\n|  O  \n| /|  \n|\n|_____",
    " _____\n|\n|  O  \n| /|\ \n|\n|_____",
    " _____\n|\n|  O  \n| /|\ \n| /   \n|_____",
    " _____\n|\n|  O  \n| /|\ \n| / \ \n|_____",
    " _____\n|  |  \n|  O  \n| /|\ \n| / \ \n|_____"]
    return step[7-chances]
'''
 _____
|  |
|  O
| /|\
| / \
|_____
'''

if __name__ == "__main__":
    main()