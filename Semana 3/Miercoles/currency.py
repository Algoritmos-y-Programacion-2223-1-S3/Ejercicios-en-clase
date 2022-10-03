currency_dict = {'euro':'€', 'dollar':'$', 'yen':'¥'}
currency_input = input("Please enter a currency name eg: Euro, Dollar or Yen: ")

print(currency_dict.get(currency_input.lower(), "Currency not found"))