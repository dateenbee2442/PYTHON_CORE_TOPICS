# List Comprehension
# fruits = ['Apple', 'Banana', 'Avocado', 'Cherry', 'Apricot']
# a_fruits = [fruit for fruit in fruits if fruit.startswith('A')]
# print(a_fruits)  # ['Apple', 'Avocado', 'Apricot']

# fruits = [
#     'Apple',
#     'Banana',
#     'Orange',
#     'Strawberry',
#     'Grapes',
#     'Watermelon',
#     'Pineapple',
#     'Mango',
#     'Blueberry',
#     'Raspberry',
#     'Peach',
#     'Pear',
#     'Plum',
#     'Cherry',
#     'Kiwi',
#     'Lemon',
#     'Lime',
#     'Grapefruit',
#     'Avocado',
#     'Papaya',
#     'Guava',
#     'Pomegranate',
#     'Cantaloupe',
#     'Honeydew',
#     'Fig',
#     'Date',
#     'Coconut',
#     'Dragonfruit',
#     'Passionfruit',
#     'Lychee'
# ]
# new_list = tuple(fruits)
# print(new_list)

fruits_with_colors = [
    {'name': 'Apple', 'color': 'Red'},
    {'name': 'Banana', 'color': 'Yellow'},
    {'name': 'Orange', 'color': 'Orange'},
    {'name': 'Strawberry', 'color': 'Red'},
    {'name': 'Grapes', 'color': 'Purple'},
    {'name': 'Watermelon', 'color': 'Green'},
    {'name': 'Pineapple', 'color': 'Yellow'},
    {'name': 'Mango', 'color': 'Yellow'},
    {'name': 'Blueberry', 'color': 'Blue'},
    {'name': 'Raspberry', 'color': 'Red'},
    {'name': 'Peach', 'color': 'Orange'},
    {'name': 'Pear', 'color': 'Green'},
    {'name': 'Plum', 'color': 'Purple'},
    {'name': 'Cherry', 'color': 'Red'},
    {'name': 'Kiwi', 'color': 'Brown'},
    {'name': 'Lemon', 'color': 'Yellow'},
    {'name': 'Lime', 'color': 'Green'},
    {'name': 'Grapefruit', 'color': 'Pink'},
    {'name': 'Avocado', 'color': 'Green'},
    {'name': 'Papaya', 'color': 'Orange'},
    {'name': 'Guava', 'color': 'Green'},
    {'name': 'Pomegranate', 'color': 'Red'},
    {'name': 'Cantaloupe', 'color': 'Orange'},
    {'name': 'Honeydew', 'color': 'Green'},
    {'name': 'Fig', 'color': 'Purple'},
    {'name': 'Date', 'color': 'Brown'},
    {'name': 'Coconut', 'color': 'Brown'},
    {'name': 'Dragonfruit', 'color': 'Pink'},
    {'name': 'Passionfruit', 'color': 'Purple'},
    {'name': 'Lychee', 'color': 'Pink'}
]
change = list(fruits_with_colors)


new_fruit = [fruit for fruit in change if 'L' in fruit['name']]
print(new_fruit)
# Output: [{'name': 'Apple', 'color': 'Red'}]