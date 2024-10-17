weight= int(input("ป้อนน้ำหนักของคุณ (kg) :"))
hight = int(input("ป้อนส่วนสูงของคุณ (cm) :"))
hight = hight / 100
#process
bmi = weight / (hight**2)
print("BMI = " , bmi)

result = "ไม่ทราบค่าที่ชัดเจน"
if bmi<= 18.0:
     result = "ต่ำกว่าเกณท์"
elif bmi>= 18.5 and bmi<=22.9:
    result = "สมส่วน"
elif bmi>= 23.0 and bmi<=24.9:
    result = "น้ำหนักเกิน"
elif bmi>= 25.0 and bmi<=29.9:
    result = "โรคอ้วน ระดับที่ 1"
elif bmi> 30:
    result = "โรคอ้วนระดับอันตราย"
else :
    result = "ไม่ทราบค่าที่ชัดเจน"

print("ค่า bmi = ", bmi ,"ทำนายว่า", result)


#control structure
#แบบทำตามลำดับ
#แบบเลือก
#แบบทำซ้ำ

#แบบเลือก
age = int(input("ป้อนอายุของคุณ : "))
if age >= 15 and age <=19 :
    print("วัยรุ่น")
elif age >= 20 and age <=29 :
    print("วัยหนุ่มสาว")
elif age >= 30 and age <=79 :
    print("วัยผู้ใหญ่")
elif age >= 80:
    print("วัยชรา")
else :
    print("วัยเด็ก")

print("จบโปรเเกรม")


#if ซ้อน if
if age <= 15:
    if age == 15:
        print("ม.3")
        #สามารถเขียนpass ได้เพื่อให้ผ่านไปก่อน
    elif age == 14:
        print("ม.2")
    elif age == 13:
        print("ม.1")
    else:
        print("ประถมศึกษา")

else: 
    print("ม.ปลาย")