class word:
    def __init__(self, text):
        self.text = text
    def reverse(self):
            return self.text [::-1]
my_word = word(input("Enter a word: "))

print(my_word.reverse())

