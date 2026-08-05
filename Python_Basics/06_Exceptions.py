# As a programmer you try to anticipate any crash that is about to happen with your code 
# and tackle it using try and exception
try:
    age = int(input("What is your age? "))
    lucky_salary = 3000
    total = lucky_salary / age
    print(f"Congratulations you salary is {total}$")

except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("Invalid input")