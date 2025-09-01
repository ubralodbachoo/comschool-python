#4
def is_pall(word):
    return word == word[::-1]

#5
import random

def generate_nicknames(word):
    suffixes = ["Master", "King", "Queen", "Wizard", "Hero", "Ninja", "Champion", "Legend"]

    nicknames = set()
    while len(nicknames) < 5:
        nick = word + random.choice(suffixes)
        nicknames.add(nick)
    return list(nicknames)

word = input("შეიყვანეთ ერთი სიტყვა: ")

nicknames = generate_nicknames(word)
print(nicknames)

#6
print("შეიყვანეთ რიცხვები გამოტოვებით:")
numbers = list(map(int, input().split()))

print(f"თქვენი რიცხვები: {numbers}")

print("\n1. ზრდადობით")
print("2. კლებადობით") 
print("3. შემთხვევითად")
print("4. უნიკალური")

choice = int(input("\nაირჩიეთ: "))

if choice == 1:
    result = sorted(numbers)
    print(f"ზრდადობით: {result}")
    
elif choice == 2:
    result = sorted(numbers, reverse=True)
    print(f"კლებადობით: {result}")
    
elif choice == 3:
    result = numbers.copy()
    random.shuffle(result)
    print(f"შემთხვევითობის პრინციპით: {result}")
    
elif choice == 4:
    result = list(set(numbers))
    print(f"უნიკალური: {result}")
    
else:
    print("შეცდომაა")
