a=1
a1=2
a2=3
a3=4
a4=5
a5=6
a6=7
a7=8
number=[1,2,3,4,5,6,7,8]
name=["นาย A","นาย B","นาย C"]
all = [10,"นาย ไข่", True ,3.14, -10]

print(name)
print(all)
print(number)

#การเข้าถึงข้อมูล

print(number[3]+number[1])
print(all[1:4])

#  #การเเก้ไขข้อมูล
print("number ก่อนแก้ไข => " , number)
number[2]=9
number[-1]="นาย ไก่"
print("หลังการแกีไข  =>" , number)

fruit = ["mango", "banana" , "Orange" , "Strawberry"]
Number=[1,2,3,4,5,6,7,8,9,10]
sum =0 
for i in range (len(fruit)):
    print(fruit[i])

fruit.append("water malon")
fruit.append("papaya")

print("หลังเพิ่ม = " , fruit)

fruit.insert(1,"durian")
print("หลังอินinsert = ", fruit)

#remove data

del fruit[2]

print("หลังremove data = ", fruit)