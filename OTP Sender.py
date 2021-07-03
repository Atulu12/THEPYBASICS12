import random
o = random.randint(10000,70000)
print(o)
otp = int(input("OTP:"))

if o == otp:
    print("Login Granted!!!")
else:
    print("Login Denied!!!")
    