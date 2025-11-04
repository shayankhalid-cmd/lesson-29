class RomanConverter:
    def int_to_roman(self, num):
        if not isinstance(num, int) or num <= 0 or num > 3999:
            return "Invalid input: Please enter an integer between 1 and 3999."

        val_symbol_pairs = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman_numeral = ""
        for value, symbol in val_symbol_pairs:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

# Example usage:
converter = RomanConverter()

print(f"The Roman numeral for 1 is: {converter.int_to_roman(1)}")
print(f"The Roman numeral for 4 is: {converter.int_to_roman(4)}")
print(f"The Roman numeral for 1994 is: {converter.int_to_roman(1994)}")
print(f"The Roman numeral for 3999 is: {converter.int_to_roman(3999)}")