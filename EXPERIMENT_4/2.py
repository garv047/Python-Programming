# 2- count vovels
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(s.count(vowel) for vowel in vowels)
print(f"Total vowels: {count}")
