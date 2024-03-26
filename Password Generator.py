import random

class PasswordGenerator:
    def __init__(self, length):
        self.length = length
    
    def generate_password(self):
        password = ''
        for i in range(self.length):
            password += random.choice(self.get_random_characters())
        return password
    
    def get_random_characters(self):
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        special_characters = '@#$'
        all_characters = uppercase_letters + lowercase_letters + digits + special_characters
        return all_characters
length = int(input("Enter the length of the password: "))
if length <= 0:
    print("Length should be greater than 0")
  
password_generator = PasswordGenerator(length)
generated_password = password_generator.generate_password()    
print("Generated Password:", generated_password)
