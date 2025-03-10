# i_got_that.py

# เริ่มต้นลูป while
while True:
    # รับข้อมูลจากผู้ใช้
    user_input = input("Enter something (type 'STOP' to exit): ")

    # ตรวจสอบว่าเป็นคำว่า "STOP" หรือไม่
    if user_input == "STOP":
        break  # หยุดลูปเมื่อกรอก "STOP"

    # ถ้าไม่ใช่คำว่า "STOP" แสดงข้อความตอบกลับ
    print(f"You said: {user_input}")
