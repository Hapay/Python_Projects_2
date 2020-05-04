import re
message = "Batmans Batmobile lost a wheel"
batRegex = re.compile(r'Bat(man|mobile|bat|copter)')
mo = batRegex.search(message)
print(mo.group())
mo2 = batRegex.findall(message)
print(mo2)