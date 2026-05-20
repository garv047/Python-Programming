# 2.
numbers = [45, 120, 88, 200, 15, 300, 50]
with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(f"{num}\n")

with open("numbers.txt", "r") as f:
    data = [int(line.strip()) for line in f if line.strip()]

if data:
    max_num = max(data)
    avg_num = sum(data) / len(data)
    count_gt_100 = len([num for num in data if num > 100])

    print(f"Max number: {max_num}")
    print(f"Average: {avg_num}")
    print(f"Count > 100: {count_gt_100}")
