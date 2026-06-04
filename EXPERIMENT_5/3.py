# 3- runner up (second largest)
n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores separated by space: ").split()))

unique_scores = sorted(set(scores), reverse=True)
runner_up = unique_scores[1]
print(runner_up)
