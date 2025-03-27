num = int(input("请输入一个数字: "))
factorial = 1
if num == 0:
    print(factorial)
else:
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)