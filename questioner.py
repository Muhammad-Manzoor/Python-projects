

import random
i = " " * 25
slNo = 1
points = 0
corAns = 0
wroAns = 0
skiAns = 0


print(i, " Number Quiz")
print("Rules")
print("-For each right answer, you will get 4 points")
print("-For each wrong answer, you will lose 2 points")
print("-There is a total of 10 questions")
print("-The quiz is out of 40 points")
print("-You can skip answers by typing 's' as the answer")
print(i)



while True:
	
	a1 = random.randint(1, 100)
	b1 = random.randint(1, 100)
	
	a2 = random.randint(1, 100)
	b2 = random.randint(1, 50)
	
	a3 = random.randint(1, 100)
	b3 = random.randint(1, 10)
	
	print("Question", slNo)
	print(i)
	
	def a4 (n):
		result = random.randint(1, 100)
		while result % n != 0:
			result = random.randint(1, 100)
		return result
	b4 = random.randint(1, 10)
	
	op = random.randint(1, 4)


	if op == 1:
		
		ans = input(str(a1) + " + " + str(b1) + " = ").upper()
		if ans == "S":
			print("You skipped the answer, the correct answer was ", a1 + b1)
			skiAns += 1
		elif int(ans) == a1 + b1:
			print("You are right")
			points += 4
			corAns += 1
		else:
			print("You are incorrect, the correct answer is ", a1 + b1)
			points += -2
			wroAns += 1
			
			
	elif op == 2:
		
		ans = input(str(a2) + " - " + str(b2) + " = ").upper()
		if ans == "S":
			print("You skipped the answer, the correct answer was ", a2 - b2)
			skiAns += 1
		elif int(ans) == a2 - b2:
			print("You are right")
			points += 4
			corAns += 1
		else:
			print("You are incorrect, the correct answer is ", a2 - b2)
			points += -2
			wroAns += 1
			
			
	elif op == 3:
	
		ans = input(str(a3) + " x " + str(b3) + " = ").upper()
		if ans == "S":
			print("You skipped the answer, the correct answer was ", a3 * b3)
			skiAns += 1
		elif int(ans) == a3 * b3:
			print("You are right")
			points += 4
			corAns += 1
		else:
			print("You are incorrect, the correct answer is ", a3 * b3)
			points += -2
			wroAns += 1
			
			
	elif op == 4:
		
		dividend = a4(b4)
		ans = input(str(dividend) + " / " + str(b4) + " = ").upper()
		if ans == "S":
			print("You skipped the answer, the correct answer was ", dividend / b4)
			skiAns += 1
		elif int(ans) == dividend / b4:
			print("You are right")
			points += 4
			corAns += 1
		else:
			print("You are incorrect, the correct answer is ", dividend / b4)			
			points += -2
			wroAns += 1
			
	if slNo == 10:
		break
	
	slNo += 1
	
	print(i)
	print(i)


print(i)

print("Correct answers : ", corAns)
print("Wrong answers : ", wroAns)
print("Skipped answers : ", skiAns)

print(i)

print("Points scored for correct answers : ", corAns * 4)
print("Points scored for wrong answers : ", wroAns * -2)

print(i)

print("Total points : ", points)








