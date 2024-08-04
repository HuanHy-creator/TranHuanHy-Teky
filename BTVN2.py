x = int(input("Nhập số bất kì:"))

if x < 0:
    print("Không phải là số nguyên tố")
elif x < 2:
    print("Không phải là số nguyên tố")
else:
    for i in range(2,x //2 +1):
        if x % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Đây là số nguyên tố")