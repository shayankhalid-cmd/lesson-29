class word:
    def __init__(self, text):
        self.text = text
    def reverse(self):
            return self.text
my_word = word(int(input("Enter a word: ")))
print(my_word.reverse())