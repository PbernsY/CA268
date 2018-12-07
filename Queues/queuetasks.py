from queue import Queue
q = Queue()
for i in range(3, 8):
	q.enqueue(i)


def rprint_queue(qinstance, front, back):
	contents = []
	while front != back:
		contents.append(qinstance.dequeue())
	return contents


def print_queue(lst, front, back):
	contents = []
	while front != back:
		current = lst[front]
		contents.append(current)
		front = (front + 1) % len(lst)
	return contents



print(rprint_queue(q, 4, 1))
print(print_queue([3, 4, 5, 6, 7], 4, 1))