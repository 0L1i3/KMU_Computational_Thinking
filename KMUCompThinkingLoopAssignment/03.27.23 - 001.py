num1 = int(input("시작값을 입력하세요: "))
num2 = int(input("끝값을 입력하세요: "))
num3 = int(input("증가값을 입력하세요: "))


i = num1
hap = 0

while i <= num2: #for i in range(num1, num2, num3):
    hap += i # hap = hap + i
    i += num3

print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" %(num1, num2, num3, hap))