amt = int(input('Enter your amount:'))

d1 = amt // 2000
amt = amt % 2000

d2 = amt // 500
amt = amt % 500

d3 = amt // 200
amt = amt % 200

d4 = amt // 100
amt = amt % 100

d5 = amt // 50
amt = amt % 50

d6 = amt // 20
amt = amt % 20

d7 = amt // 10
amt = amt % 10

total = d1+d2+d3+d4+d5+d6+d7
print(f'Total number of notes needed for representing that amount:{total}')