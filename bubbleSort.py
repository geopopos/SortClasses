def swap(list, i, a, b):
	c = list[i][b]
	list[i][b] = list[i][a]
	list[i][a] = c

	return list


def bubbleSort(days, timeValues):
	for i in range(0, len(days)):
		for j in range(0, len(days[i])-1):
			for k in range(0,len(days[i])-1):
				if timeValues[days[i][k]] > timeValues[days[i][k+1]]:
					days = swap(days, i, k, k+1);