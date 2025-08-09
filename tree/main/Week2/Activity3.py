class StringManipulator:
    # def __init__(text):
    #     self.text = text

    def find_character(text, char):
        return text.find(char)
    
    def string_len(text):
        return len(text)
    
    def convert_uppercase(text):
        return text.upper()

name = "example"

result = StringManipulator.find_character(name, 'a')

length = StringManipulator.string_len(name)

upper = StringManipulator.convert_uppercase(name)

def main():
    print(result)
    print("name length: ", length)
    print("convert_uppercase: ", upper)

if __name__ == "__main__":
    main()