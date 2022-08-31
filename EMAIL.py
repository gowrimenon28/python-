import re
pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
user_id=input('enter the email id:')
if re.search(pattern,user_id):
    print('valid email id')
else:
    print('invalid email id')    
