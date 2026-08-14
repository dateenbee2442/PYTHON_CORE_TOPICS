def student_info():
    student = {}
    student['name'] = input('What is your name: ')
    student['surname']= input('What is your surname: ')
    student['age']= int(input('Age: '))
    student['phone']= input('Phone number: ')
    student['major']= input('Major: ')
    student['graduation_year']= int(input('Graduation year: '))
    student['status'] = input('What is your status (single/married): ')
    student['country']= input('Country: ')

    print("\n--- STUDENT INFORMATION ---")
    for key, value in student.items():
        print(f'{key}: {value}'.capitalize())
    print('* ' *10)
    

student_result = {
    'Maths': 90,
    'chinese': 98,
    'DSA': 80,
    'linear Algebra': 98,
    'DBMS': 89,
    'Python': 99
}

student_info()



# student_info['status'] = 'single'
# student_info.update(student_result)



# # print(student_info)
# # print(student_info.values())
# # print(student_info)