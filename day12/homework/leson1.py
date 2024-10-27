i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

    sum = 0
i = 1
while sum < 50:
    sum += i
    i += 1
print("ჯამი:", sum)

number = int(input("შეიტანეთ რიცხვი: "))
if number % 2 == 0:
    print("რიცხვი არის ლუწი.")
else:
    print("რიცხვი არის კენტი.")

    score = int(input("შეიტანეთ ქულა: "))
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
elif 0 <= score < 60:
    print("Grade F")
else:
    print("არასწორი ქულა.")

    age = int(input("შეიტანეთ თქვენი ასაკი: "))
if age < 13:
    print("You are a kid")
elif 13 <= age < 20:
    print("You are a teenager")
else:
    print("You are grown up")
git push
sandro boy
sandro04300