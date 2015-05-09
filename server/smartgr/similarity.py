import numpy as np
from munkres import Munkres, print_matrix, make_cost_matrix
import sys, math

def ckn(query1, query2):
	cnum = 0
	term1 = query1.split(',')
	term2 = query2.split(',')
	for x in term1:
		for y in term2:
			if x == y:
				cnum = cnum + 1

#	print cnum
	return cnum

def kn(query):
	term = query.split(',')
	return len(term)

def maxmatching(matrix):
	cost_matrix = []
	for row in matrix:
		cost_row = []
		for col in row:
#			cost_row += [sys.maxsize - col]
			cost_row += [10 - col]
		cost_matrix += [cost_row]

	m = Munkres()
	indexes = m.compute(cost_matrix)
	print_matrix(matrix, msg='Highest profit through this matrix:')
	total = 0

	for row, column in indexes:
		value = matrix[row][column]
		total += value
		print '(%d, %d) -> %f' % (row, column, value)

	print 'total profit=%f' % total
	print

def simi(query1, query2):
	return round( ( float(ckn(query1, query2)) / (max(kn(query1),kn(query2))) ), 4 )

def summatrix(matrix):
	csum = 0
	for row in matrix:
		for col in row:
			csum = csum + col

	print csum

################################################################################

query1 = "python,test,case"
query2 = "python"

#print max(kn(query1),kn(query2))

#ckn(query1, query2)


queryA1 = "python,test,case"
queryA2 = "python,test,driven"
queryA3 = "python,framework"
queryA4 = "test,driven,development"
queryA5 = "test,framework"

queryB1 = "test,driven"
queryB2 = "python,tutorial"
queryB3 = "python,example"
queryB4 = "python,library"
queryB5 = "python,test,case"

queryC1 = "test,manual"
queryC2 = "python,implementation"
queryC3 = "python,source,code"
queryC4 = "python,package"
queryC5 = "python,test,case"

queriesA = [queryA1, queryA2, queryA3, queryA4, queryA5]
queriesB = [queryB1, queryB2, queryB3, queryB4, queryB5]
queriesC = [queryC1, queryC2, queryC3, queryC4, queryC5]

#bgraph = np.arange(25).reshape((5,5))
matrix = [[0.0]*5 for x in xrange(5)]

for i, x in enumerate( queriesA ):
	for j, y in enumerate( queriesB ):
		matrix[i][j] = simi(x, y)*100
"""
for i in xrange(0,len(queriesA)):
	for j in xrange(0,len(queriesB)):
		print (matrix[i][j]),' ',
	print
"""
print 'similarity between a and b'
maxmatching(matrix)

matrix2 = [[0.0]*5 for x in xrange(5)]

for i, x in enumerate( queriesA ):
	for j, y in enumerate( queriesC ):
		matrix2[i][j] = simi(x, y)*100

print 'similarity between a and c'
maxmatching(matrix2)


matrix3 = [[0.0]*5 for x in xrange(5)]

for i, x in enumerate( queriesB ):
	for j, y in enumerate( queriesC ):
		matrix3[i][j] = simi(x, y)*100

print 'similarity between b and c'
maxmatching(matrix3)

summatrix(matrix)
summatrix(matrix2)
summatrix(matrix3)
