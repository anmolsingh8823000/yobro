import random

def prefRandOut(list):

	#initialising sum variable
	sum = 0

	#calculating the sum cumulative priorities of
	for row in list:
		sum = sum + row[1]    #calculating sum of priorities
		row.append(sum)       #calculating cumulative priorities

	#getting random float between 0 and the sum
	r = random.uniform(0,sum)

	#initialising variable i
	i = 0

	#iterating through each row
	while (i<len(list)):

		#checking if this row is selected by random variable
		if(r<=list[i][2]):

			#returning the chosen row
			return list[i]

		i = i + 1
