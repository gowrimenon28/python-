import re
number=input()
pattern=r"(1|8|9)[0-9]+"
match=re.match(pattern,number)
if len(number)==8:
    if(match):
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")           
