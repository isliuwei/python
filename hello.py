
num = input("enter a num:\n")
i=0;
while num != 8 and i < 3:
	num = input("enter a num:\n")

	if num == 8:
		print("yes")
	else:
		i = i + 1
		print(i)
		if num < 8:
			print("small")
		else:
			print("big")

print("end")


	


