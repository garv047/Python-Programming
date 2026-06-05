# 5- movie dictionary
n = int(input("Enter number of movies: "))
movies = []

for g in range(n):
    name = input("Movie name: ")
    year = int(input("Year: "))
    movies.append({
        "name": name,
        "year": year,
    })

print("\n(a) All movie details:")
for m in movies:
    print(m)

print("\n(b) Movies released before 2015:")
for m in movies:
    if m["year"] < 2015:
        print(m["name"])
