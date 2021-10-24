money = int (input('enter amount of money:'))
apple = int (input ('price of apple:'))

total= money // apple
change= money - total * apple

print(input(f'you can buy {total} apples and your change is {change} pesos '))