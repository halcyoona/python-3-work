def div(n1, n2):
	return n1 / n2

#print (div(4, 2))	


def sortlist(lst):
	alist = lst[:]
	for passnum in range(len(lst) - 1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
	return alist