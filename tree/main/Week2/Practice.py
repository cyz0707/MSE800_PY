import random
WORDS = ("spicy", "sweet", "salt", "bitter", "sour",  "umami")

def generateRandomWord():
    return random.choice(WORDS)

def getAnswer(word):
    answer = []
    for letter in word:
        answer.append(letter)
    return answer

def generateGuessBoard(puzzle):
    print(puzzle)

def guessWord(word, answer, result):
    
    guess = input("please input a letter: ")
    if len(guess) != 1 :
        guessWord(word, answer, result)
    else:
        trying = result

        if guess in word:
            print(answer.index(guess))
            trying[answer.index(guess)] = guess
        
        else:
            print("Lose a life")
        # if (word.index(guess) >= 0):
        # print(trying, answer)
        if (trying == answer):
            return
        else:
          print(trying)
          guessWord(word, answer, trying)

def practice():
    word = generateRandomWord()
    answer = getAnswer(word)
    result = []
    for letter in word:
        result.append("")
    guessWord(word, answer, result)
    # return puzzle

if __name__ == "__main__":
    answer = practice()
    print("\n Final result:", answer)
