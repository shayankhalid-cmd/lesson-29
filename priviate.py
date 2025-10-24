class myclass:
    __privatevar = 27;
    def __privmeth(self):
        print("im inside class myclass")
    def hello(self):
        print("priviate varaiable value:", myclass.__privatevar)
foo = myclass()
foo.hello()
foo.__privmeth