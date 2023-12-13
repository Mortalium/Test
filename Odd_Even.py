import random

for i in range(0,100):
	x=random.randint(0,100)
	if x%2 != 0:
		print("{} ist Ungerade".format(x))
	elif x%2 == 0:
		if x==0:
			print("{} ist halt 0".format(x))
		else:
			print("{} ist Gerade".format(x))