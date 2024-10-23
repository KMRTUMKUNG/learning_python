# def sayhi():
#     print("halo Function")

# def Thailand():
#     print("สวัสดี ชาวไทย.")

# def English():
#     print ("hellow / hi!!")

# def sumer():
#     x = 3+1
#     print(x)

# sumer()

import random
words =  ("ค้อน", "กรรไกร", "กระดาษ")
i = 0

print("คุณมีโอกาส ตีกับบอท 3 ครั้งเท่านั้น!! เเพ้ = กาก")
for i in range (1,4):
    print()
    print("รอบที่ = " , i)
    myrandom = random.choice(words)
    print("เกมเป่ายิ่งฉุบ!!")
    answer = str(input("ค้อน กรรไกร กระดาษ จะออกอะไร!! ตอบ: "))
 
    if answer == myrandom:
        print("เสมอนะครับบ~~~")

    elif answer == "กรรไกร"  and myrandom == "ค้อน":
        print("คุณแพ้!! เพราะบอทออก" , myrandom)

    elif answer == "ค้อน"  and myrandom == "กระดาษ":
        print("คุณแพ้!! เพราะบอทออก" , myrandom)
    elif answer == "กระดาษ"  and myrandom == "กรรไกร":
        print("คุณแพ้!! เพราะบอทออก" , myrandom)
    else :
        print("คุรชนะ เพราะบอทออก", myrandom)
        break
    

print("จบโปรเเกรม!!")

    
   
# print("คำตอบคือ = ", myrandom) 
           

       
    # if not correct :
    #     print("เสียใจด้วยยย")
    #     print("เฉลย = " , myrandom)