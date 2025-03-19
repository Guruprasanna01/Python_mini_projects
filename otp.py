import random
def generate_otp():
    return str(random.randint(1000, 9999))

otp = generate_otp()
print("Your OTP is:", otp)

