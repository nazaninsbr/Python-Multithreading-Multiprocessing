import threading 

def calc_power(base, power):
	print(base**power)

if __name__ == '__main__':
	number = 7
	thread1 = threading.Thread(target=calc_power, args=(number, 2))
	thread2 = threading.Thread(target=calc_power, args=(number, 4))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()