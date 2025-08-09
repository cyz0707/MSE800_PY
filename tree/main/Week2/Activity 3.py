class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def string_len(self):
        return len(self)
    
    def convert_uppercase(self):
        return self.upper()

name = StringManipulator("example")

result = StringManipulator.find_character(name, 'a')

length = StringManipulator.string_len('aaa')

upper = StringManipulator.convert_uppercase('aaa')

print(result)
print("name length: ", length)
print("convert_uppercase: ", upper)