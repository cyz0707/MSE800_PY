def word_count(s):
    if not s:
        return 0
    if isinstance(s, list):
        return len(s)
    words = s.split()
    return len(words)

def uppercase_count(s):
    if not s:
        return 0
    if isinstance(s, list):
        return sum(1 for word in s for char in word if char.isupper())
    return sum(1 for char in s if char.isupper())

str = "Hello, how are you?"
arr = ["Hello", "how", "are", "you"]

print(word_count(str), uppercase_count(str))
print(word_count(arr), uppercase_count(arr))
