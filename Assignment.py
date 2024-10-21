a = int(input("ป้อนตัวเลขที่ 1 :"))
b = int(input("ป้อนตัวเลขที่ 2 :"))
if a>b :
    print(a  , "มากกว่า" , b)
else:
    print(b , "มากกว่า" , a)

number = int(input("ป้อนตัวเลขของคุณ :"))
if number % 2 == 0:
    print("เป็นเลขคู่ ")
else: 
    print("เป็นเลขคี่")

monney = int(input("ป้อนจำนวนเงินของคุณ"))

if monney >= 1000:
    print("1000 bath = ", monney//1000 , "ใบ")
    monney = monney % 1000

if monney >= 500:
    print("500 bath = ", monney//500 , "ใบ")
    monney = monney % 500

if monney >= 100:
    print("100 bath = ", monney//100 , "ใบ")
    monney = monney % 100

if monney >= 50:
    print("50 bath = ", monney//50 , "ใบ")
    monney = monney % 50

if monney >= 20:
    print("20 bath = ", monney//20 , "ใบ")
    monney = monney % 20
   

#แปลง ปี ค.ศ. เป็น พ.ศ. +543
#แปลง ปี พ.ศ. เป็น ค.ศ. -543

start , stop = 1,3
sum ,avg =0 , 0
while (start<=stop):
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum+= number
    start+= 1

avg = sum/stop
print("ผลรวม = ", sum)
print("ค่าเฉลี่ย = " , avg)


