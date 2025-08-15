class File:
    def __init__(self, url):
        self.url = url
    
    def readFile(self):
        data = open(self.url)
        return data.readlines()
    
    def writeFile(self):
        with open(self.url, 'w') as file:
            file.write('hello world! line 12 3')      

def main():
    file = File('demo.txt')
    lines = File.readFile(file)

    File.writeFile(file)

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()

