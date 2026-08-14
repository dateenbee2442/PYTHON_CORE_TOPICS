# IF statements
job = input("What is your skill: ")
years_of_experience = int(input("What is you years of experience: "))

if job.capitalize() == 'Python':
    print('Your skill is really required!!')
elif years_of_experience >= 6:
    print('Years of experience also matched')
else:
    print('You meet non of the requirement')