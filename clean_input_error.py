def inp_num(type_num): 
	'''Функция возвращает либо целое, либо вещественное введенное число. Проверяет правильность ввода.
	При вх 1 - проверяет, что введенное число целое.
	При вх 0 - проверяет, что введенное число вещественное, а не буквы или знаки.'''
	ind=0
	while ind==0:
		if type_num==1: #целое
			try:
				num=int(input('n='))
				ind=1
			except:
				ind=0
				print('Повторите ввод')

		elif type_num==0:
			try:
				num=float(input('n='))
				ind=1
			except:
				ind=0
				print('Повторите ввод')
		else:
			print('В функции inp_num указан неверный вх параметр (может быть 0 или 1)')
	return num