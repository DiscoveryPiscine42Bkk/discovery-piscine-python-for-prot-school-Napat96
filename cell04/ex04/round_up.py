#!/usr/bin/env python3

import math  # ใช้สำหรับฟังก์ชันปัดเศษขึ้น

# ขอให้ผู้ใช้ป้อนตัวเลข และแปลงเป็น float
num = float(input("Give me a number: "))

# ปัดเศษขึ้น
rounded_num = math.ceil(num)

# แสดงผลลัพธ์
print(f"The rounded-up number is: {rounded_num}")
