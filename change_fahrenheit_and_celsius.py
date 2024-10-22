temp = input("ป้อนอุณหภูมิ (องศา) :")

degree = int(temp[:-1])
unit = temp[-1].upper()

print(degree , "=" , unit)

if unit =="C":
    result=(9*degree)/5+32
    unit_result ="fahrenheit"
if unit =="F":
    result=(degree-32)*5/9
    unit_result ="celsius"

print("แปรงตัวเลข = ", temp , "เป็น" ,unit_result , "=" ,result)