number = []
Number = []

while True:
     x = int(input("ป้อนตัวเลขของคุณ : "))
     if x < 0 :
          break
     number.append(x)
     
     
print(" ")

print("ก่อนเรียง => ", number)
number.sort()
print("หลังเรียงน้อยไปมาก => ", number)
number.reverse()
print("หลังเรียงมากไปน้อย => ", number)
print(" ")

print("ค่าที่มากที่สุด => ", max(number))
print("ค่าที่น้อยที่สุด => ", min(number))
print("ผลรวม => ",sum(number))

print(" ")

khu = []
khee =[]

print("โปรแกรมเเยก เลขคู่ เลขคี่ ")
while True:
     x = int(input("ป้อนตัวเลขของคุณ : "))
     if x < 0 :
          break
     if x%2 ==0 :
          khu.append(x)
     else :
          khee.append(x)
     Number.append(x)
     
print("ตัวเลขทั้งหมด => " , Number)
print("ตัวเลขคู่ => " , khu)
print("ตัวเลขคี่ => " , khee)

print(" ")
print(Number)
for i in range(len(Number)):
     Number[i] = Number[i]**2
print(Number)

fruit = ["mango", "water melon", "strawberry", "blue berry"]
price = [50,30,25,40,]

for x,y in zip(fruit,price):
     print("สินค้า = ",x , "ราคา = ", y)

massage = ["aa","sa","cda","asd","wea","era"]
result =[]

for item in massage:
     result.append(item.count("a"))

print(result)