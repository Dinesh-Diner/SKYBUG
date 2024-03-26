'''
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"
    
    def mod(self):
        if self.b != 0:
            return self.a % self.b
        else:
            return "Cannot modulo by zero"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter operator (+, -, *, /, %): ")
calculator = Calculator(num1, num2)

if op == '+':
    result = calculator.add()
elif op == '-':
    result = calculator.sub()
elif op == '*':
    result = calculator.mul()
elif op == '/':
    result = calculator.div()
elif op == '%':
    result = calculator.mod()

print("Result:", result)
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
print("Generated Password:", generated_password)'''
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found in the list.")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Thank you for using the To-Do List application!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()





  
