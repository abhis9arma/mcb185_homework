
def accuracy(tp, fp, tn, fn):
	acc = (tp + tn)/(tp + fp + tn +fn)
	rec = (tp)/(tp + fn)
	pre = (tp)/(tp + fp)
	f = ((pre * rec)/(pre + rec)) * 2
	print(acc, f)
	
	
print(accuracy(25, 5, 65, 5))
print(accuracy(5, 25, 5, 65))
print(accuracy(45, 15, 80, 20))
		
		
		