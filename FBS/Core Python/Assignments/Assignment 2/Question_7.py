dig = int(input('Enter your number:'))

d1 = dig % 10
dig = dig // 10

d2 = dig % 10
dig = dig // 10

d3 = dig % 10
dig = dig // 10

print(f'Addition of your digit is:{d1+d2+d3}')