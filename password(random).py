import random
pwd_len=int(input("Enter the length of the password:"))
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits="0123456789"
spe_char="!@#$%^&*()~`?+[];,"
setters=[]
for i in range(pwd_len):
    l=random.choice(letters)
    setters.append(l)
    d=random.choice(digits)
    setters.append(d)
    s=random.choice(spe_char)
    setters.append(s)
pwd=''
pwd+=''.join(setters)
password=''
for j in range(pwd_len):
    password+=''.join(random.choice(pwd))
print(password)
