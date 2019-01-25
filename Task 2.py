Num = int(input("Enter Number: "))
Reverse = 0
while (Num > 0):
    Reminder = Num % 10
    Reverse = (Reverse * 10) + Reminder
    Num = Num // 10

print("\n Reverse Number is = %d" % Reverse)