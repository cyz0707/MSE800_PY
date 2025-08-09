import random
WORDS = ("spicy", "sweet", "salt", "bitter", "sour",  "umami")
LIFE = 3

def generateRandomWord():
    return random.choice(WORDS)

def getAnswer(word):
    answer = []
    for letter in word:
        answer.append(letter)
    return answer

def guessWord(word, answer, blanks, life): 
    guess = input("please input a letter: ")
    if len(guess) != 1 :
        guessWord(word, answer, blanks, life)
    else:
        trying = blanks
        if guess in word:
            print(answer.index(guess))
            trying[answer.index(guess)] = guess
        else:
            life -= 1
            print("Lose a life!")
            if life == 0:
                print("You lose!")
                return

        # check answer
        if (trying == answer):
            print("you win!")
            return
        else:
          print(trying)
          guessWord(word, answer, trying, life)

def play():
    word = generateRandomWord()
    answer = getAnswer(word)
    blanks = []
    for letter in word:
        blanks.append("")
    guessWord(word, answer, blanks, LIFE)

if __name__ == "__main__":
    answer = play()
    print("\n Final result:", answer)
