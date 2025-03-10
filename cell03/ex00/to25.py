# to25.py

user_input = int(input("Enter a number:\n"))


if user_input > 25:
    print("Error")
else:
    # สร้างลูปเพื่อแสดงตัวเลขจาก input ถึง 25
    for i in range(user_input, 26):
        print(i)
