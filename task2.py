num = input('Введите трехзначное число: ')
flag = True
while flag:    
    if num.isdigit()!=True or len(num) !=3:
        num = input('Неверно, введите трехзначное число: ')
    else:
        flag=False
num=int(num)
a=num//100
b=((num//10)%10)
c=num%10
sum=a+b+c
print(f'{a} + {b} + {c} = {sum}')
