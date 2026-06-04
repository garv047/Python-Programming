# 4- name-city
n = int(input("Enter number of persons: "))
people = {}

for _ in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    people[name] = city

print("All names:")
for name in people.keys():
    print(name)

print("All city names:")
for city in set(people.values()):
    print(city)

print("Name and city of all students:")
for name, city in people.items():
    print(name, ":", city)

city_count = {}
for city in people.values():
    city_count[city] = city_count.get(city, 0) + 1

print("Number of students in each city:")
for city, count in city_count.items():
    print(city, ":", count)
