# Develop a project using class and methods to get a sentence from user 
# input and find the number of words in it. Share your GitHub link at the end.

class WordsCount:
    def __init__(self, text):
        self.text = text

    def count(self):
        return len(self.text.split())

def main():
    sentence = input("please input a sentence: ")
    words = WordsCount(sentence)
    print(WordsCount.count(words))

if __name__ == "__main__":
    result = main()
    print("\n Final result:", result)