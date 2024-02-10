#47deathsaves.py by Abhi Sharma
import random

dead = 0
revived = 0
stable = 0
limit = 10000

for i in range(limit):
	failure = 0
	success = 0
	while failure < 3 and success < 3:
		d1 = random.randint(1, 20)
		if d1 == 1:
			failure += 2
		elif d1 == 20:
			revived += 1
			failure = 0
			success = 0
		elif d1 < 10:
			failure += 1
		else:
			success += 1
	if failure >= 3:
		dead += 1
	if success >= 3:
		stable += 1
		
total = dead + stable + revived
probdead = dead / total
probstable = stable / total
probrevived = revived / total
	
print(probdead)
print(probstable)
print(probrevived)	