# 4- substring occurance
string = input("Enter main string: ")
substring = input("Enter substring: ")
count = 0
start = 0
while True:
    pos = string.find(substring, start)
    if pos == -1:
        break
    count += 1
    start = pos + 1
print(count)
