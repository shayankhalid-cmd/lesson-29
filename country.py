class japan():
    def capital(self):
        print("Tokyo is the capital of Japan")
    def language(self):
        print("japansese is the official language of Japan")
    def type(self):
        print("Japan is a developed country")
class india():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the official language of India")
    def type(self):
            print("India is a developing country")
obj_japan = japan()
obj_india = india()
for country in (obj_japan, obj_india):
    country.capital()
    country.language()
    country.type()