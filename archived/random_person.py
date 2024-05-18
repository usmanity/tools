from random import randrange

# people = str(input("Please enter the names for the choices (comma separated): "))

print("Picking people from text file")
file = open('people.txt', 'r')
people = file.read().split(',')

#people = people.split(',')

while (len(people)):
    enter = input("\nPress enter when ready")
    random_index = randrange(0, len(people))
    person = people.pop(random_index)
    print("Pick " + person.strip() + " for this task!!")
