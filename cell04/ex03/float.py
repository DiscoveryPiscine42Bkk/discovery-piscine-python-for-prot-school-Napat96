#!/usr/bin/env python3

# ขอให้ผู้ใช้ป้อนตัวเลข และแปลงเป็น float
num = float(input("Give me a number: "))

# ตรวจสอบว่าค่าที่ป้อนเป็นจำนวนเต็มหรือทศนิยม
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
