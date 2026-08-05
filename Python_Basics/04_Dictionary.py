# This code return the requested info to the viewer from the dictionary of a customer
customer = {
    'name': 'Ahmad Datin',
    'age': 22,
    'phone': '08137244286',
    'address': 'katsina state, nigeria',
    'product': 'Phone',
    'model': 'Samsung',
    'payment_method': 'Transfer',
    'payment_status': True,
    'doo': '7-7-26',
    'edoo': '20-7-26'

}

# for key, value in customer.items():
#     message = f"{key} : {value}".title()
    
#     print(message)

message = input("What information do you want to know about the customer? ").split()

for word in message:
    result = customer.get(word, 'not found')
    print(f'{word} : {result}')
