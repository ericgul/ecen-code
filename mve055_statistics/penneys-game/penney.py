import random as rand

a = [0,1,0,1]
b = [1,0,1,1]

#Returns the expected number of steps taken until specified sequence is reached.
#SS is sample size, the number of rounds to run the experiment before calculating average
def getExpectedHistoryLength(sequence, ss):
	seqLen = 0
	history = []
	full_history = []
	k = len(sequence)
	for i in range(0, ss):
		while (True):
			r = rand.randint(0,1)
			history.append(r)
			full_history.append(r)
			if (len(history) >= k+1):
				for j in range(1, k+1):
					history[j-1] = history[j]
				history = history[0:k]
			if (history == sequence):
				seqLen += len(full_history)
				history = []
				full_history = []
				break
	return seqLen / ss

#Simulate n rounds of penneys game where 
#   player 1 chooses sequence A every time and
#   player 2 chooses sequence B every time.
#Sequence A and B are required to have the same length.
def penneySim(a, b, n):
	history = []
	full_history = []
	awins = 0
	bwins = 0
	k = len(a)
	for i in range(0, n):
		while (True):
			r = rand.randint(0,1)
			history.append(r)
			full_history.append(r)
			if (len(history) >= k+1):
				for j in range(1, k+1):
					history[j-1] = history[j]
				history = history[0:k]
			if (history == a):
				awins += 1
				history = []
				full_history = []
				break
			if (history == b):
				bwins += 1
				history = []
				full_history = []
				break			
	print("A: %d" %awins)
	print("B: %d" %bwins)

def expectedTimes(a, s, n):
	history = []
	full_history = []
	awins = 0
	counter = 0
	k = len(a)
	for i in range(0, n):
		for l in range(0, s):
			#print(full_history)
			r = rand.randint(0,1)
			counter += 1
			#print(len(history))
			history.append(r)
			full_history.append(r)
			if (len(history) >= k+1):
				for j in range(1, k+1):
					history[j-1] = history[j]
				history = history[0:k]
			if (history == a):
				awins += 1
				#print("%d: win" %counter)
				print(":: " + str(history))
			#elif (len(history) <= 3):
			#	print("%d: ??" %counter)
			#else:
			#	print("%d: --" %counter)
		full_history = []
	return awins/n
	
def expectedTimes2(seq, k):
	tr = 0
	for i in range(0, k):
		coinTosses = []
		for j in range(0, 100):
			r = rand.randint(0,1)
			coinTosses.append(r)
			#print(coinTosses)
		for l in range(4,100+1):
			curSeq = coinTosses[l-4:l]
			#print(str(l) + " : " + str(curSeq))
			if (curSeq == seq):
				tr += 1
				
	#print("tr = " + str(tr))
	#print(" k = " + str(k))
	return tr/k

#penneySim(a, b, 100000)
#print("E[A]: %.3f" %getExpectedHistoryLength(a, 100000))
#print("E[B]: %.3f" %getExpectedHistoryLength(b, 100000))

def binPlusOneList(list):
	k = len(list)
	top = 1
	for i in range(0, k):
		if (list[i] == 0 and top == 1):
			list[i] = 1
			top = 0
		elif (list[i] == 1 and top == 1):
			list[i] = 0
			top = 1
	return list
			
list = [0,0,0,0]
for i in range(0, 16):
	print("Current: " + str(binPlusOneList(list)))
	print("Number of A on 100: %.3f" %expectedTimes2(list, 100000))