#2) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
x = 5
y = 10
print("ჯამი:", x + y)

#3) შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია.
#კომენტარი: სტრინგების შეერთებას ეწოდება კონკატენაცია.
str1 = "გამარჯობა"
str2 = "მეგობარო"
print("კონკატენაცია:", str1 +" "+ str2)

#4) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი.
x = 10
y = 2
print("განაყოფი:", x / y)

#5) შედარების ოპერატორები:
print(5 == 5)   # ტოლობა
print(3 != 4)   # უთანასწორობა
print(7 > 2)    # მეტობა
print(5 < 10)   # ნაკლებობა
print(6 >= 6)   # მეტობა ან ტოლობა
print(8 <= 10)  # ნაკლებობა ან ტოლობა

#6) შედარების ოპერატორები და მათემატიკური ოპერაციები:
print(5 + 5 == 8 + 2)

#7) ლოგიკური ოპერატორები (სულ 8 კომბინაცია):
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#8) ლოგიკური და შედარების ოპერატორები:
print(5 > 3 and 2 < 4)
print(10 == 10 or 5 > 15)
print(7 != 5 and 4 > 2) 
print(6 >= 6 or 3 < 2)
print(not(5 == 5)) 

#9) for loop 1-დან 10-მდე რიცხვების დასაბეჭდად:
for i in range(1, 11):
    print(i)

#10) list-ის რიცხვების ჯამის გამოსათვლელად:
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for num in numbers:
    total_sum += num
print("ჯამი:", total_sum)

#11) for loop თითოეული სიმბოლოს დასაბეჭდად სტრინგში:
string = "Hello, World!"
for char in string:
    print(char)
#12) while loop 1-დან 10-მდე რიცხვების დასაბეჭდად:
i = 1
while i <= 10:
    print(i)
    i += 1

#13) while loop რომელიც გამოტოვებს რიცხვებს 50-დან 60-მდე:
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

#14) while loop რომელიც ითვლის რიცხვებს სანამ ჯამი არ გახდება 50:
i = 1
total = 0
while total < 50:
    total += i
    i += 1
print("ჯამი:", total)

#15) მომხმარებლის შეყვანილი რიცხვი შემოწმდეს 3-ზე ან 5-ზე იყოფა თუ არა:
num = int(input("შეიყვანეთ რიცხვი: "))
if num % 3 == 0 or num % 5 == 0:
    print(f"{num} იყოფა 3-ზე ან 5-ზე")
else:
    print(f"{num} არ იყოფა 3-ზე ან 5-ზე")

#16) საშუალო არითმეტიკულის გამოთვლა რიცხვების სიიდან:
numbers = [1, 3, 4, 5, 2]
average = sum(numbers) / len(numbers)
print("საშუალო:", average)

#17) სტრინგის ყოველი მეორე ასო დაწერილი იყოს დიდი ასოთი:
s = "hello"
result = ""
for i in range(len(s)):
    if i % 2 == 0:
        result += s[i].upper()
    else:
        result += s[i].lower()
print(result)

#18) სიიდან რიცხვების კვადრატების გამოთვლა:
numbers = [3, 12, 5, 2, 6]
squared_list = []
for num in numbers:
    squared_list.append(num ** 2)
print(squared_list)