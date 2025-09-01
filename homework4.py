#1
import random
import string

length = int(input("პაროლის სიგრძე: "))

use_lower = input("გამოვიყენო პატარა ასოები (y/n)? ")
use_upper = input("გამოვიყენო დიდი ასოები (y/n)? ")
use_digits = input("გამოვიყენო ციფრები (y/n)? ")
use_symbols = input("გამოვიყენო სიმბოლოები (y/n)? ")

chars = ""

if use_lower.lower() == "y":
    chars += string.ascii_lowercase
if use_upper.lower() == "y":
    chars += string.ascii_uppercase
if use_digits.lower() == "y":
    chars += string.digits
if use_symbols.lower() == "y":
    chars += string.punctuation

if chars == "":
    print("უნდა აირჩიო მაინც ერთი სიმბოლოების ჯგუფი!")
    exit()

password = ""
for i in range(length):
    password += random.choice(chars)

print("გენერირებული პაროლი:", password)

#2
pwd = input("შეიყვანე პაროლი: ")
score = 0

if len(pwd) >= 8:
    score += 3
elif len(pwd) >= 5:
    score += 1

for ch in pwd:
    if ch.isdigit():
        score += 3
        break

for ch in pwd:
    if ch.islower():
        score += 1
        break

for ch in pwd:
    if ch.isupper():
        score += 3
        break

if score > 10:
    score = 10

if score <= 3:
    strength = "weak"
elif score <= 6:
    strength = "medium"
else:
    strength = "strong"

print(f"ქულა: {score}/10 → {strength}")

#3

def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < num:
        fib.append(fib[-1] + fib[-2])
    return fib