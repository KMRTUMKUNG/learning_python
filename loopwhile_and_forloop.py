i = 0
sum = 0

while i <= 5:
    sum +=i 
    i +=1
    print("รอบที่ = " , i ,"sum = " , sum )

print("\n")

num = 0
for l in range(1,11): # 0, 1, 2 (start ,stop-1 ,step)
    num += l
    print("รอบที่ = " , l , "num = " , num)

print("ผลรวม = " , num)
print("ค่าเฉลี่ย = " , num/10)

print("\n")

for j in range(10,0,-1): # 0, 1, 2 (start ,stop-1 ,step)
    num -= l
    print("รอบที่ = " , j , "num = " , num)

print("ผลรวม = " , num)
print("ค่าเฉลี่ย = " , num/10)


   