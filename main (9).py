a= int(input('Введите 5 значное число')) 
if 47811 > a < 10330: 
 print('Число подходит') 
 b = a // 1000 
 c = a % 1000 
 print('Первое число', b, 'Второе число', c) 
else: 
 print('Некоректное число')