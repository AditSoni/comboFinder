# creating a Dictionary from the given csv file..
import random as r
def combo(d_path,low1,high1):
	fp=open(d_path)
	D={}
	x=0
	for line in fp:
		if x==0:
			x=1
			continue
		l=line.split(',')
		D[l[0]]=int(l[1].strip())




	


	result=set()
	setlb=2           # least elements in a combo
	setub=len(D)      # max items in a combo
	loops=6000   
	low=low1           # lower bound of cost
	high=high1          # upper bound of cost
	for i in range(loops):
		SetSize=r.randint(setlb,setub)
    
		x=r.sample(list(D.values()),SetSize) # using list 'coz we need a sequence or set
		x.sort()
		chromosome=tuple(x)
    
		if sum(chromosome) in range(int(low),int(high+1)): # if the selected products fall in range
			l=[]                                 # creating alist to store product names
			for i in chromosome:                 # this takes each price and finds corresponding product
				k=[key for key, value in D.items() if value == i][0] # list comprehension used to extract
                                                                 #  keys using given value
				l.append(k)
			l=tuple(l) # list is not hashable so we need to convert list into tuple
			result.add(l)
	
	return result