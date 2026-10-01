import random
import string

val=string.ascii_letters+string.digits+string.punctuation
password=""
pass_len=12

for i in range(pass_len):
    password+=random.choice(val)
print("Your password is : ",password)

#list comprehension
# res="".join([random.choice(val) for i in range(pass_len)])
# print(res)

