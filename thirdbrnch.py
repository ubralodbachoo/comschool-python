#7
text = input("შეიყვანეთ ტექსტი: ")

filter = ''.join(i for i in text if i.isalpha() or i.isspace())

print("გაფილტრული ტექსტი:", filter)

#8
num_lst = list(map(int, input("შეიყვანეთ რიცხვები: ").split()))

while len(num_lst) > 1:
    print(num_lst)
    num_lst = [num_lst[i] + num_lst[i+1] for i in range(len(num_lst)-1)]
print(num_lst)

#9 
text1 = input("შეიყვანე ტექსტი: ").lower().split()
word_count = {}
for word in text1:
    word_count[word] = word_count.get(word, 0) + 1

#10
text2 = input("შეიყვანე ტექსტი: ").lower().split()
char_count = {}
for i in text2:
    char_count[i] = len(i)

