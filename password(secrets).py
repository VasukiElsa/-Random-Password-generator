import secrets
import string
pwd_len=int(input("Enter password length to be create:"))
letters=string.ascii_letters
digits=string.digits
special_chars=string.punctuation
setter=letters+digits+special_chars
pwd=''
for i in range(pwd_len):
    pwd+=''.join(secrets.choice(setter))
print(pwd)
