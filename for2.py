#การเขียนโปรแกรมแบบกำหนดจำนวนรอบทำซ้ำ for ด้วยการรับค่าข้อมูลผ่านตัวแปร
cicle = int(input("ป้อนจำนวนรอบ ? "))
j = 0;
for i in range (cicle):
    j = j + 1
    print("รอบที่ i="+str(i)+" j="+str(j))
