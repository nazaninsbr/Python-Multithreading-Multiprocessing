import multiprocessing 

result = []

def calc_square(numbers):
	global result
	for n in numbers:
		result.append(n*n)
	print('inside process: '+str(result))

def problem():
	numbers = [1, 2, 3]
	p = multiprocessing.Process(target=calc_square, args=(numbers, ))
	p.start()
	p.join()
	print('outside process: '+str(result))

def calc_square_changed(numbers, result2):
	for idx, n in enumerate(numbers):
		result2[idx] = n*n
	print('inside process: ')
	print(result2[:])

def solution():
	numbers = [1, 2, 3]
	result2 = multiprocessing.Array('i', 3)
	p2 = multiprocessing.Process(target=calc_square_changed, args=(numbers, result2))
	p2.start()
	p2.join()
	print('outside process: ')
	print(result2[:])

if __name__ == '__main__':
	problem()
	solution()