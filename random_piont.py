import random

myrandom = random.randrange(1,7)
k=1

correct = False
print("คุณมีโอกาสตอบ 3 ครั้ง \n")

while True:
    number = int(input("ป้อนคำตอบของคุณ = "))
   
    correct = (number == myrandom)

    if not correct :
         if (number>myrandom):
            print("น้อยกว่านี้ นิสน้อย")
         if (number<myrandom):
            print("มากกว่านี้นิสน้อยย")

    if correct :
         print("คำตอบถูกต้อง รับไปเลย ไก่ 1 ตัว")
         break
    if number<0 or k==3:
            break
    # else :
    #      print("เสียใจด้วยย อดกินไก่!!!")
    k+=1
if not correct :
    print("เสียใจด้วยยย")
    print("เฉลย = " , myrandom )

