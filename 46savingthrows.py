#46SavingThrows by Abhi Sharma
import random


#DifficultyClass5 Saving Throw
limit = 1000
safe1 = 0
total1 = 0

#normal5
for i in range(limit):
	d1 = random.randint(1, 20)
	if d1 >= 5:
		safe1 += 1
	total1 += 1
probsafe1 = safe1 / total1


#advantage5
safe2 = 0
total2 = 0 
for i in range(limit):
	d2 = random.randint(1, 20)
	d3 = random.randint(1, 20)
	if d2 >= d3 and d2 >= 5:
		safe2 += 1
	if d3 > d2 and d3 >= 5:
		safe2 += 1
	total2 += 1
	probsafe2 = safe2 / total2


#disadvantage5
safe3 = 0
total3 = 0 	
for i in range(limit):
	d4 = random.randint(1, 20)
	d5 = random.randint(1, 20)
	if d4 <= d5 and d4 >= 5:
		safe3 += 1
	if d5 < d4 and d5 >= 5:
		safe3 += 1
	total3 += 1
	probsafe3 = safe3 / total3


#normal10
safe4 = 0
total4 = 0
for i in range(limit):
	d1 = random.randint(1, 20)
	if d1 >= 10:
		safe4 += 1
	total4 += 1
probsafe4 = safe4 / total4


#advantage10
safe5 = 0
total5 = 0 
for i in range(limit):
	d2 = random.randint(1, 20)
	d3 = random.randint(1, 20)
	if d2 >= d3 and d2 >= 10:
		safe5 += 1
	if d3 > d2 and d3 >= 10:
		safe5 += 1
	total5 += 1
	probsafe5 = safe5 / total5


#disadvantage10
safe6 = 0
total6 = 0 	
for i in range(limit):
	d4 = random.randint(1, 20)
	d5 = random.randint(1, 20)
	if d4 <= d5 and d4 >= 10:
		safe6 += 1
	if d5 < d4 and d5 >= 10:
		safe6 += 1
	total6 += 1
	probsafe6 = safe6 / total6


#normal15
safe7 = 0
total7 = 0
for i in range(limit):
	d1 = random.randint(1, 20)
	if d1 >= 15:
		safe7 += 1
	total7 += 1
probsafe7 = safe7 / total7


#advantage15
safe8 = 0
total8 = 0 
for i in range(limit):
	d2 = random.randint(1, 20)
	d3 = random.randint(1, 20)
	if d2 >= d3 and d2 >= 15:
		safe8 += 1
	if d3 > d2 and d3 >= 15:
		safe8 += 1
	total8 += 1
	probsafe8 = safe8 / total8


#disadvantage15
safe9 = 0
total9 = 0 	
for i in range(limit):
	d4 = random.randint(1, 20)
	d5 = random.randint(1, 20)
	if d4 <= d5 and d4 >= 15:
		safe9 += 1
	if d5 < d4 and d5 >= 15:
		safe9 += 1
	total9 += 1
	probsafe9 = safe9 / total9

	
#Table

print("DC", "norm", "adv", "dis", sep="\t")
print(5, probsafe1, probsafe2, probsafe3, sep="\t")
print(10, probsafe4, probsafe5, probsafe6, sep="\t")
print(15, probsafe7, probsafe8, probsafe9, sep="\t")