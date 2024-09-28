
i = (" ")*25


print(i, "Reverse order")
print("-When you type words or sentences it will be shown in reverse order")

while True:
	
	a = input("Word : ")
	ans = a[::-1]
	
	print(ans)
	print(i)
	
	y = input("Do you want to continue? (y/n) ").upper()
	print(i)
	print(i)
	
	if y != "Y":
		break
	
