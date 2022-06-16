# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2

combined_string_lower = combined_string.lower()


t = combined_string_lower.count('t')
r = combined_string_lower.count('r')
u = combined_string_lower.count('u')
e = combined_string_lower.count('e')

word_true = t + r + u + e


l = combined_string_lower.count('l')
o = combined_string_lower.count('o')
v = combined_string_lower.count('v')
e = combined_string_lower.count('e')

word_love = l + o + v + e

result = int(str(word_true)+str(word_love))
print(f'your score is {result}')

if result < 10 or result > 90:
    print(f'your love score is {result}, you go together like coke and mentos')
elif result >=40 and result <=50:
    print(f'your love score is {result}, you are alright together')
else:
    print(f'your love score is {result}')
