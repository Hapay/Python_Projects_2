# RE USED AT THE END! Tutaj jest kod jesli nie uzywalibysmy regular expressions
# We have American phone number. xxx-xxx-xxxx Napisac funkcje która będzie sprawdzala czy numer jest poprawny

def isPhoneNumber(number):
    if len(number) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not number[i].isdecimal():
            return False  # no area code
    if number[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not number[i].isdecimal():
            return False  # no first 3 digits
    if number[7] != '-':
        return False  # missing 2nd dash
    for i in range(8, 12):
        if not number[i].isdecimal():
            return False  # no 2nd four digits
    return True
print(isPhoneNumber("415-123-4567"))
print("\n")

# Mamy jakis tekst i chcemy w nim wyszukac wszystkie numery telefonu dzieki naszej funkcji
message = "Call me on 415-123-4567 or at 415-987-6543 for my office line, today "
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        foundNumber = True
if not foundNumber:
    print("Could not find any phone numbers")
    print("\n")
print("\n")

# NOW SHORTER VERSION USING REGULAR EXPRESSIONS
import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(mo.group()+"\n")  # Wyswietla nam tylko pierwszy numer. Jesli chcemy wszystkie to uzywamy zamiast "search" "findall" i tylko
#print(mo)