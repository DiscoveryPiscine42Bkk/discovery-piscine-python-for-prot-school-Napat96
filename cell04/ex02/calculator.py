#!/usr/bin/env python3

# ขอให้ผู้ใช้ป้อนตัวเลขสองตัว และแปลงเป็นตัวเลขทศนิยม
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# คำนวณผลลัพธ์
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# ตรวจสอบการหารเลขศูนย์
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# แสดงผลลัพธ์
print(f"\nResults:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
