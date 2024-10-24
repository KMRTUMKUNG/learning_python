sub = ()
score = 0
grade = [4,3.5,3,2.5,2,1.5,1,0]
i = 0
print ("==Program_studentgrade==")

while i <= 0:
    sub = input("ป้อนชื่อวิชา : ")
    score = int(input("ป้อนคะเเนนที่ได้รับ :"))
    

    if score <= 100:
        print("วิชา" , sub , "ได้คะเเนน" , score)
        if score >= 80:
            print("คุณได้เกรด : " , grade[0])
        
        elif score >= 75:
            print("คุณได้เกรด : " , grade[1])
        
        elif score >= 70:
            print("คุณได้เกรด : " , grade[2])
        
        elif score >= 65:
            print("คุณได้เกรด : " , grade[3])

        elif score >= 60:
            print("คุณได้เกรด : " , grade[4])

        elif score >= 55:
            print("คุณได้เกรด : " , grade[5])

        elif score >= 50:
            print("คุณได้เกรด : " , grade[6])
        
        elif score <= 49:
            print("คุณตกวิชานี้ คุณได้เกรด : " , grade[7])
    else:
        print("คุณใส่คะเเนนไม่ถูกต้องงงง")
        
  