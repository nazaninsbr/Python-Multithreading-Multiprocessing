import time 
import multiprocessing 

def deposit(balance):
	for i in range(100):
		time.sleep(0.01)
		balance.value = balance.value + 1


def withdraw(balance):
	for i in range(100):
		time.sleep(0.01)
		balance.value = balance.value - 1

def problem():
	balance = multiprocessing.Value('i', 200)
	d = multiprocessing.Process(target=deposit, args=(balance, ))
	w = multiprocessing.Process(target=withdraw, args=(balance, ))

	d.start()
	w.start()

	d.join()
	w.join()
	# it should print 200 but it does not
	print("After transactions: ", balance.value)


def deposit_solution(balance, lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		balance.value = balance.value + 1
		lock.release()


def withdraw_solution(balance, lock):
	for i in range(100):
		time.sleep(0.01)
		lock.acquire()
		balance.value = balance.value - 1
		lock.release()


def solution():
	balance = multiprocessing.Value('i', 200)
	lock = multiprocessing.Lock()
	d = multiprocessing.Process(target=deposit_solution, args=(balance, lock))
	w = multiprocessing.Process(target=withdraw_solution, args=(balance, lock))

	d.start()
	w.start()

	d.join()
	w.join()
	# it should print 200 but it does not
	print("After transactions: ", balance.value)

if __name__ == '__main__':
	problem()
	solution()