#get all the indexes of a number in a list

[index for index,value in enumerate(l) if value == 1]

#split list with given number of elements
f = lambda A,n : [A[i:i+n] for i in range(0,len(A),n)]
f(A)
