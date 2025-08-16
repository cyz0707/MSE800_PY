class FileProcessing:
    def __init__(self, url):
        self.url = url
    
    def readFile(self):
        file = open(self.url)
        data = file.read()
        file.close()
        return data

    def countWords(self):
        data = FileProcessing.readFile(self)
        print(len(data.split()))

def main():
    file = FileProcessing('demo.txt')
    FileProcessing.countWords(file)

if __name__ == "__main__":
    main()