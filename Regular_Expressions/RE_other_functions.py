import re
allDigitsRegex = re.compile(r'^\d+$')
# + oznacza "one or more"
# ^ oznacza, ze ma sie zaczynac wartoscia liczbowa
# $ oznacza, ze ma sie konczyc wartoscia liczbowa
# mo means "matching object"
# * oznacza 0 lub wiecej
msg = '13236343267457345345'
mo = allDigitsRegex.search(msg)
print(mo)

msg2 = '123252343asd1236865645'
mo2 = allDigitsRegex.search(msg2)
print(mo2) # It does not match the pattern
print("")


# . kropka oznacza, ze znajdzie slowa i wypisze przed ta koncowka jeden znak
#dotRegex = re.compile(r'.at')
dotRegex = re.compile(r'.{1,2}at') # tutaj jeden LUB dwa znaki!
msg3 = 'The cat in the hat sat on the flat mat'
mo3 = dotRegex.findall(msg3)
print(mo3)
print("")


# .* oznacza wyszukiwanie czegokolwiek
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
msg4 = 'First Name: Patryk Last Name: Majchrzak'
mo4 = nameRegex.findall(msg4)
print(mo4) # Z racji tego, że mamy dwa nawiasy to wyswietli liste, a w niej tuple
print("")


# * zachowuje sie greedy, co oznacza, ze wyswietli wszystko co jest podane w funkcji
# *? zachowuje sie nongreedy czyli wyswietli tylko to co pasuje do funkcji i przestanie
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>') # szukamy czegokolwiek jesli tylko zaczyna i konczy sie <>
print(nongreedy.findall(serve))
print("")


# . kropka wyswietla wszystko, ale jesli cos jest w nowej linii to juz tego nie wyswietli
prime = "Serve the public trust.\n Protect the innocent.\nUpload the law."
print(prime)
dotStarRegex = re.compile(r'.*', re.DOTALL)
print(dotStarRegex.findall(prime))