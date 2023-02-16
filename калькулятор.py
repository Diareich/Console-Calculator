# Уринный калькалятор v2.1

from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()

print (Fore.BLACK)



while True:
	print (Back.RED)
	print ("Вас приветствует Уринный калькалятор v2.1")
	
	print (Back.WHITE)
	print ("Для выхода нажмите: Q")

	print (Back.GREEN)
	print ("Что делаем?\n(+ (Сложение), - (Вычитание),\n* (Умножение), / (Деление),\n** (Степень), % (Остаток от деления)): ")
	what = input ("Выберите знак операции которую хотите произвести:")

	if what.lower () == "q":
		break # выход из цикла

	if what == "+":
		print (Back.CYAN)
		print ("a + b = c")
		a = float (input ("Введите первое число (a): "))
		b = float (input ("Введите второе число (b): "))
		c = a + b
		print (Back.YELLOW)
		print ("Результат:", c)

	elif what == "-":
		print (Back.CYAN)
		print ("a - b = c")
		a = float (input ("Введите первое число (a): "))
		b = float (input ("Введите второе число (b): "))
		c = a - b
		print (Back.YELLOW)
		print ("Результат:", c)

	elif what == "*":
		print (Back.CYAN)
		print ("a * b = c")
		a = float (input ("Введите первое число (a): "))
		b = float (input ("Введите второе число (b): "))
		c = a * b
		print (Back.YELLOW)
		print ("Результат:", c)

	elif what == "/":
		print (Back.CYAN)
		print ("a / b = c")
		a = float (input ("Введите первое число (a): "))
		b = float (input ("Введите второе число (b): "))
		c = a / b
		print (Back.YELLOW)
		print ("Результат:", c)

	elif what == "**":
		print (Back.CYAN)
		print ("a**b = c")
		a = float (input ("Введите число которое хотите возвести в степень (a): "))
		b = float (input ("Введите степень в которое число будет возводится (b): "))
		c = a ** b
		print (Back.YELLOW)
		print ("Результат:", c)

	elif what == "%":
		print (Back.CYAN)
		print ("a % b = c")
		a = float (input ("Введите первое число (a): "))
		b = float (input ("Введите второе число (b): "))
		c = a % b
		print (Back.YELLOW)
		print ("Результат:", c)

	else:
		print ("Выбранна невераная операция!")