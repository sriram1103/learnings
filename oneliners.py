#get all the indexes of a number in a list

[index for index,value in enumerate(l) if value == 1]

#split list with given number of elements
f = lambda A,n : [A[i:i+n] for i in range(0,len(A),n)]
f(A)

#dict sort by value
sorted_d = sorted(d.items(), key=lambda (k,v): v)
#python 3
sorted(list(d.items()),key = lambda v:v[1] ))
#^^ because d.items() return dict view
