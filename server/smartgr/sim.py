import numpy as np
from munkres import Munkres, print_matrix, make_cost_matrix
import sys, math

debug = 0

def ckn(query1, query2):

#	print 'query1',
#	print query1
#	print 'query2',
#	print query2

	cnum = 0
	term1 = query1.split(',')
	term2 = query2.split(',')

##	print 'term1 ',
##	print term1
##	print 'term2 ',
##	print term2
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
			cost_row += [10 - col]
		cost_matrix += [cost_row]

	m = Munkres()
	indexes = m.compute(cost_matrix)
	if debug == 1:
		print_matrix(matrix, msg='Highest profit through this matrix:')
	total = 0

	prev = 0
	maxIdx = None
	for row, column in indexes:
		value = matrix[row][column]
		total += value
		if debug == 1:
			print '(%d, %d) -> %f' % (row, column, value)
		if prev < value:
			prev = value
			maxIdx = [row,column]

	if debug == 1:
		print 'total profit=%f' % total
		print

	return total, maxIdx


def simi(query1, query2):
	return round( ( float(ckn(query1, query2)) / (max(kn(query1),kn(query2))) ), 4 )



################################################################################

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

curSet= [queryA1, queryA2, queryA3, queryA4, queryA5]

totalSet = {}
totalSet['queriesB'] = [queryB1, queryB2, queryB3]#, queryB4, queryB5]
totalSet['queriesC'] = [queryC1, queryC2, queryC3, queryC4]#, queryC5]

def getMaxMatching(curSet, totalSet, threshold):
	# Check len of both Set
	# add extra 0 to smaller set
	matrix = None

##	print 'CurSet'
##	print curSet
##	print
##	print 'TotalSet'
##	print totalSet

	maxSet = {}

	tkeys = totalSet.keys()
	for tkey in tkeys:
		queriesT = None
		maxsize = max( len(curSet), len(totalSet[tkey]) )
		minsize = min( len(curSet), len(totalSet[tkey]) )

		if maxsize != minsize:
			if len(curSet) > len(totalSet[tkey]):
				queriesT = totalSet[tkey]
			else:
				queriesT = curSet

			for _ in xrange(0, (maxsize-minsize)):
				queriesT.append("")


		matrix = [[0.0]*maxsize for _ in xrange(maxsize)]
		for i, x in enumerate( curSet ):


			for j, y in enumerate( totalSet[tkey] ):
				if debug == 0:
					matrix[i][j] = simi(','.join(x.queries), ','.join(y.queries))*100
				else:
#					matrix[i][j] = simi(','.join(x), ','.join(y))*100
#					print i, ';', j, '?', (simi(x, y) * 100 + 100000)
					matrix[i][j] = simi(x, y)*100
#					print matrix[i][j]

		
#		print matrix

		maxSet[tkey] = maxmatching(matrix)

	maxValue = 0
	tkeys1 = maxSet.keys()
	maxKey = None
	maxIdx = None
	for tkey1 in tkeys1:
		if maxValue < maxSet[tkey1][0]:
			matSize = len(matrix)
			if threshold <= (maxSet[tkey1][0] / matSize):
				maxValue = maxSet[tkey1][0]
				maxKey = tkey1
				maxIdx = maxSet[tkey1][1]

#	print 'Max:', maxValue, maxKey, maxIdx
#	print totalSet[maxKey][maxIdx[1]]

#	print maxSet
	return maxKey, maxIdx


if __name__ == "__main__":
	"""
	mSet = getMaxMatching(curSet, totalSet)
	tkeys1 = mSet.keys()
	for tkey1 in tkeys1:
		print tkey1, mSet[tkey1]
	"""
	mKey, mIdx = getMaxMatching(curSet, totalSet, 10)
	print mKey, mIdx
	print totalSet[mKey][mIdx[1]]

