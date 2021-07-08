# lists

people = ["Clara", "Fares", "Karim"]

print(people)

# using negative index gives result from last to first

print(people[-1])
print(people[-2])
print(people[-3])
print(people[0])

# the ':' sets the range of list selection

print(people[2:])
print(people[0:2])

# list functions

family = ["Marcelinho", "Lauro"]
people.extend(family)

print(people)

people.append("Morgana")

print(people)

people.insert(1, "Zeina")

print(people)

people.sort()

print(people)

people.remove("Morgana")

print(people)

people.pop()

print(people)

print(people.index("Clara"))

my_people = people.copy()

people.clear()

print(people)
print(my_people)
