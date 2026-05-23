# 3.
with open("city.txt", "w") as f:
    f.write("Dehradun 5.78 308.20\n")
    f.write("Delhi 190 1484\n")
    f.write("Mumbai 124 603.4\n")
    f.write("Shimla 1.7 25\n")
    f.write("Bangalore 84 709\n")

total_area = 0

with open("city.txt", "r") as f:
    lines = f.readlines()

print("Details of all cities:")
for line in lines:
    parts = line.split()
    if len(parts) == 3:
        name = parts[0]
        pop = float(parts[1])
        area = float(parts[2])

        print(f"City: {name}, Population: {pop}L, Area: {area} sq KM")

        total_area += area

print("\nCities with population > 10 Lakhs:")
for line in lines:
    parts = line.split()
    if len(parts) == 3:
        name = parts[0]
        pop = float(parts[1])
        if pop > 10:
            print(name)

print(f"\nSum of areas of all cities: {total_area} sq KM")
