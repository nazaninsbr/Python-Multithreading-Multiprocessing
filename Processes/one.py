import multiprocessing 

def calc_power(base, power):
	print('Number: ', base)
	result = base**power
	print('Result: ', result)

if __name__ == '__main__':
	result = 0
	p1 = multiprocessing.Process(target=calc_power, args=(7, 2))
	p2 = multiprocessing.Process(target=calc_power, args=(11, 4))

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	print('result is: ', result)