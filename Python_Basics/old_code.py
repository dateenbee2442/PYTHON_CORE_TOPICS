# secret_no = 4
# no_of_try  = 0
# while no_of_try < 3:
#    select_no = int(input("Guess a number: "))
#    no_of_try = no_of_try + 1
#    if select_no == secret_no:
#       print("Congratulations you win!!")
#       break
# else:
#    print (f'Sorry you tried {no_of_try} times and failed')

# instruction = ""
# started = False
# while True:
#     instruction = input('> ').lower()
#     if instruction == 'start':
#         if started:
#             print('Car is already started!')
#         else:
#             started = True
#             print("Car started..... ready to go")
#     elif instruction == 'stop':
#         if not started:
#             print('Car is already off!')
#         else:
#             started = False
#             print("Car stopped..... pussssss")
#     elif instruction == 'help':
#         print("""
# Start - to start the car
# Stop - to stop the car
# Quit - to exit
#         """)
#     elif instruction == 'quit':
#         break
#     else:
#         print("Sorry I don't understand what you mean")

# prices = [1,2,3,4,5,6]
# total = 0
# for x in prices:
#     total += x
# print(total)

# numbers = [5,2,5,2,2]
# for number in numbers:
#     space = 'x'
#     for y in space:
#         print(y*number)
# numbers = [1,2,3,12,30, 1,4,6,]
# max = numbers[0]
# for number in numbers:
    
#     if number> max:
#         max = number
# print(max)

# phone_list = ['samsung', 'iphone', 'pixel', 'samsung', 'xiaomi', 'iphone', 'redmi', 'huawei', 'apple', 'apple']
# available = []
# print("The sold out phones: ")
# for phone in phone_list:
#     if phone not in available:
#         available.append(phone)
#     else:
#         print(f'sold out {phone.title()}')
# UNPACKING
# a,b,c,d,e,f,g = available
# print(f'Do you need {a} or {b}, or {c}')
# location = [20, 30, 13, 33]
# a,b,c,d = location
# print(b*a)
# customer = {"name": "Ahmad Datin",
#             'phone': '08137244286',
#             'payment': True,
#             'method': 'cash',
#             "order": "Pixel 7pro",
#             'date of order': '7-7-26',
#             'expected date of delivery': '20-7-26'}
# ask = input('What do you want to know about the customer: ').split()

# for keyword in ask:
#     result = customer.get(keyword, 'not found')
#     print(f'{keyword} : {result}')

# phone = input('Phone: ')
# digit_translator = {
#     '0': 'Zero',
#     '1': 'One',
#     '2': 'Two',
#     '3': 'Three',
#     '4': 'Four', 
# }
# output = " "
# for cha in phone:
#     output = output + digit_translator.get(cha, '!') + " "
# print(output)
customer = {}
print("Hi!! welcome to our online shopping.")

customer['name'] = input("Enter customer name: ")
customer['age'] = input("Enter your age: ")
customer['phone number'] = input("Enter phone number: ")
customer['order'] = input("Enter phone model ordered: " )
customer['payment_method'] = input("Payment method: ")

print('Customers details')
for key, value in customer.items():
    print(f'{key} : {value}')