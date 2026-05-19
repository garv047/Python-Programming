# 1.
with open("name.txt", "w") as f:
    f.write("Alice\nEve\nIsaac\nOscar\nUma\nBob\nCharlie")

with open("name.txt", "r") as f:
    names = [line.strip() for line in f if line.strip()]

count_names = len(names)

vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
vowel_count = len([name for name in names if name.startswith(vowels)])

longest_name = max(names, key=len) if names else ""

print(f"Total names: {count_names}")
print(f"Names starting with a vowel: {vowel_count}")
print(f"Longest name: {longest_name}")
