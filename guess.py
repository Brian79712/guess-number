import random

r = random.randint(1, 100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('恭喜你~猜對啦! ')
		break 
	if num < r:
		print('比答案小!')
	if num > r:
		print('比答案大!')