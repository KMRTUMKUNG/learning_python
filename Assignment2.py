sum =0 

while sum <= 100:
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum+= number
    
print("ผลรวม = ", sum)

print("\n")


max , min = 0 , 9999

while True :
    number = int(input("ป้อนตัวเลขของคุณ : "))

    if number<0 :
        break
    
    if number > max :
        max = number

    if number< min :
        min = number

print("ค่าสูงสุด = ", max)
print("ค่าต่ำสุด = ", min)

last = int(input("ป้อนตัวเลขของคุณ : "))

for row in range(1, last+1):
    for colum in range(1 ,row+1):
        print(colum , end = '')
    print(" ")