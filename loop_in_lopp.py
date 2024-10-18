i=0
while i<=3:
    j=1
    while j<=5:
        print("รอบที่ = " , i ,"ตำแหน่งที่ = " , j)
        j+=1
    i+=1

print ("\n")

for i in range (1,4):
    print("รอบที่ = " , i)

    for j in range(1,6):
     print("ตำแหน่งที่ = " , j)
     j+=1
    i+=1

print ("\n")

for x in range (2,5):
    print ("\n")
    print("แม่ = " , x)

    for y in range(1,13):
     print(x ,"x" ,y ," = "  , (x*y))
     
#break หลุดออกจสก loop continue โดดข้าม
print ("\n")

for i in range (1,20):
   if(i%2 != 0 ):
     continue
   
   if (i == 18):
    break
   print("รอบที่ = ", i)

print("จบโปรแกรม")