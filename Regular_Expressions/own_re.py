import re
#Tutaj stworzona klasa regex przeze mnie
vowelRegex = re.compile(r'[aeiouyAEIOUY]')

# Two vowels in a row
#vowelRegex = re.compile(r'[aeiouyAEIOUY]{2}')

#This will match every char that isn't in a char class
#vowelRegex = re.compile(r'[^aeiouyAEIOUY]')

message = "2019 Microsoft Corporation. All rights reserved."
mo = vowelRegex.findall(message)
print(mo)

unique = []
for word in mo:
    if word not in unique:
        unique.append(word)
print(unique)
