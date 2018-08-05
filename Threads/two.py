import threading 

class Worker(threading.Thread):
	def __init__(self):
		super(Worker, self).__init__()

	def run(self):
		for i in range(10):
			print(i)

if __name__ == '__main__':
	thread1 = Worker()
	thread2 = Worker()
	thread3 = Worker()
	thread1.start()
	thread2.start()
	thread3.start()