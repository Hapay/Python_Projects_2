#Jesli chcemy posegregowac np ten numer na region i liczby
import re
message = "Call me at 415-123-4567 today "
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(message)
print(mo.group(2))

mess = "Call me at (415) 123-4567 today "
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex.search(mess)
print(mo2.group())