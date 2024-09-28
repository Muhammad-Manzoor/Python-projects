
t="   "*13
s="  "*5
Score =0
def i():
    print(s)

i()
print("%s Quiz"%t)
i()

print(" Rules:")
print("-There are two questions.")
print("-There will be four options for each qustion.")
print("-You can *only type the lowercase version of the option you are choosing.")
print("*You can't enter anything else.")
print("-You will get one mark for each right answer.")
print("-Here is an example: 10) Which is the biggest country in the world?")
print("                     a) USA     %s b) China"%s)
print("                     c) Cannada %s d) Russia"%s)
print("                     Your answer: d")



i()
i()
print("Let's begin.")
i()

print("1) What has hands but cannot clap?")
print("a) Human %s b) Animal"%s)
print("c) Clock %s d) Bucket"%s)
while True:
 a=input("Your answer: ")

 if a == "c":
     i() 
     print("You are correct and you get one mark.")
     Score +=1
     break
 
 elif a in ["a", "b", "d"]:
     i()
     print("Sorry the right answer is c.")
     break
 
 else :
     print("You didn't enter the proper value.")
     i()
     continue



i()
i()
print("Next question.")
i()

print("2) I am an odd number. Take away a letter and I become even. What am I?")
print("a)5  %s b)7"%s)
print("c)10 %s d)11"%s)
while True:
 b=input("Your answer: ")
 
 if b == "b":
     i() 
     print("You are correct and you get one mark.")
     Score +=1
     break
 
 elif b in ["a", "c", "d"]:
     i() 
     print("Sorry the right answer is b.")
     break
 
 else :
     print("You didn't enter the proper value.")
     i()
     continue
 


i()
i()
print("There are no more questions left.")
i()
print("This is your score.")
print("your score is: ", Score )
i()
i()
i()