num = int(input('Enter any three digit number you want to reverse:'))
d1= num % 10
num = num // 10

d2= num % 10
num = num // 10

d3= num % 10
num = num // 10

print(f'The reverse digits is:{d1}{d2}{d3}')