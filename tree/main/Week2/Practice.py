import random
WORDS = ("spicy", "sweat", "salt", "best", "sour", "python", "apple", "look")
LIFE = 3

def generateRandomWord():
    return random.choice(WORDS)

def getAnswer(word):
    answer = []
    for letter in word:
        answer.append(letter)
    return answer

def checkAnswer(word, answer, trying, life):
    if (trying == answer):
        print(f"You win! The answer is {word}")
        return
    else:
        show = ""
        for item in trying:
            if item == "":
                show += "__ "
            else:
                show = f"{show}{item} "
        print(show)
        guessWord(word, answer, trying, life)    

def guessWord(word, answer, blanks, life): 
    guess = input("please input a letter: ")
    if len(guess) != 1 :
        guessWord(word, answer, blanks, life)
    else:
        trying = blanks
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    trying[i] = guess
        else:
            # check remaining life
            life -= 1
            print("Lose a life!")
            if life == 0:
                print("You lose!")
                return

        checkAnswer(word, answer, trying, life)

def play():
    word = generateRandomWord()
    answer = getAnswer(word)
    blanks = [""] * len(word)
    guessWord(word, answer, blanks, LIFE)

if __name__ == "__main__":
    play()
