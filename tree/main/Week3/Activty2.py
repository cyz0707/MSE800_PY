class FileProcessing:
    def __init__(self, url):
        self.url = url
    
    def readFile(self):
        data = open(self.url)
        return data.readlines()

    def countWords(self):
        lines = FileProcessing.readFile(self)
        wordNum = 0
        for line in lines:
            wordNum += len(line.split())
        print(wordNum)    

def main():
    file = FileProcessing('demo.txt')
    FileProcessing.countWords(file)

if __name__ == "__main__":
    main()