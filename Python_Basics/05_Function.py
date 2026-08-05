# def greet_users(x, y):
#     print(f'Hi {x}, the requested product: {y} is now being examined.....')

# name = input("Hi please input your name: ")
# model= input("Input the model you want to buy: ")
# greet_users(name, model)
#

# make a function that returns what ever kind of greatings

def greetings(message):
    words = message.split()
    emoji = {
        ":)" : "(00)",
        "):": ")00("
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input(">")
result = greetings(message)
print(result)