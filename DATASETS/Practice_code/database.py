
def database(name, age, country):
    return {
    'name' : name,
    'age' : age,
    'country' : country
    }

def show_database(students):
     print("-"*45)
     print("            Student Database")
     print("-"*45)
     print(f"{"Name":<20} | {'Age':<5} | {'Country':<20}")
     print("_"*50)
     for stu in students:
        print(f"{stu['name']:<20} | {stu['age']:<5} | {stu['country']}")


def load_data():
    s1 = database("adil", 22, 'Pakistan')
    s2 = database("Usman Khang", 22, 'China')
    s3 = database("Ahmad", 22, 'Malaysia')
    s4 = database("MUhammad", 22, 'Nigeria')
    s5 = database('Ali', 24, "China")
    s6 = database('Usman', 23, "NIgeria")
    students = [s1,s2,s3,s4,s5,s6]
    return students 

students = []
while True:
    print("\n-------------Students Database Management___________")
    print("1.Show Database\n2.Load Database\n3.Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        if not students:
            print(f"Your Database is Empty: {students}\n")
        else: 
            show_database(students)
    elif choice == "2":
        students = load_data()
        print("Your Data Successfully Loaded ✅")
    elif choice == "3":
        print("Thanks for practice👌")
        break
    else:
        print("Invalide Number!")