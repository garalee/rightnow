from dbmanager.Dao import DB
from model import GroupDataModel
from bson.objectid import ObjectId
import datetime

from bson.code import Code


class TotalDao:
	def insertQueries(self,user_id, queries):
		words_collection = DB.Words

		w = {}
		w['user_id'] = user_id
		w['queries'] = queries
		w['date'] = datetime.datetime.utcnow()

		return words_collection.insert(w)


	def getWordsByUserID(self,userID ):
		a = DB.Words.find({"user_id": ObjectId(userID)})

		wordsSet = []
		words = None

		for i in a:
			words = GroupDataModel.Words()
			words.queries = i['queries']
#			words.keywords = i['keywords']
			words.ID = i['_id']
			words.user_id = i['user_id']
			wordsSet.append(words)

		return wordsSet

	def getOthersWordsByUserID(self, userID):
		othersWords = DB.Words.find({"user_id": {"$ne": ObjectId(userID)}}).sort("user_id")

		totalSet = {}
		wordsSet = []

		for usr in othersWords:
			wordsSet = self.getWordsByUserID(usr['user_id'])
			totalSet[usr['user_id']] = wordsSet

		return totalSet

	""" origin
	def getOthersWordsByUserID(self,userID ):
		othersWords = DB.Words.find({"user_id": {"$ne": ObjectId(userID)}}).sort("user_id")

		wordsSet = []
		words = None
		tempUser = ''

		for i in othersWords:
			words = GroupDataModel.Words()
			words.queries = i['queries']
#			words.keywords = i['keywords']
			words.ID = i['_id']
			wordsSet.append(words)
#			print words.queries

		return wordsSet

	"""


	def insertWords(self,words):
		words_collection = DB.Words

		w = {}
		w['keywords'] = sorted(words.keywords)
		w['queries'] = sorted(words.queries)

		return words_collection.insert(w)











	def insertGroup(self,group):
		group_collection = DB.Group
		g = {}
		g['wordsID'] = group.wordsID
		return group_collection.insert(g)
		
	def selectWordsByQueries(self,queries):
		words_collection = DB.Words

		w = {}
		w['queries'] = sorted(queries)

		a = DB.Words.find(w)

		words = None

		for i in a:
			
			words = GroupDataModel.Words()
			words.queries = i['queries']
			words.keywords = i['keywords']
			words.ID = i['_id']

		return words
		

	def selectWordsByKeywords(self,keywords):
		words_collection = DB.Words
		
		k = {}
		k['keywords'] = sorted(keywords)
		
		a = DB.Words.find(k)

		words = None
		
		for i in a:
			words = GroupDataModel.Words()
			words.queries = i['queries']
			words.keywords = i['keywords']
			words.ID = i['_id']
			
		return words
		

	def selectWordsByQueriesAndKeywords(self,queries,keywords):
		words_collection = DB.Words

		w = {}
		w['queries'] = sorted(queries)
		w['keywords'] = sorted(keywords)

		a = DB.Words.find(w)

		words = None

		for i in a:
			words = GroupDataModel.Words()
			words.queries = i['queries']
			words.keywords = i['keywords']
			words.ID = i['_id']

		return words

	def selectGroupByWordsID(self,wordsID):
		group_collection = DB.Group
		a = group_collection.find({"wordsID" : ObjectId(wordsID)})

		g = None

		for i in a:
			g = GroupDataModel.Group()
			g.ID = i['_id']
			g.wordsID = i['wordsID']

		return g
	
	def selectGroupByID(self,groupID):
		group_collection = DB.Group
		a = group_collection.find({"_id": ObjectId(groupID)})

		g = None
 
		for i in a:
			g = GroupDataModel.Group()
			g.ID = i['_id']
			g.wordsID = i['wordsID']

		return g

	def selectGroupByUserID(self,userID):
		group_collection = DB.UserJoin
		#%print 'userID: ',userID
		a = group_collection.find({"userID":ObjectId(userID)}).sort( [('date', -1)] )

		g = None
		gr = []

 		#%print '1. gr: ', gr

		for i in a:
			g = GroupDataModel.Group()
			g.ID = i['_id']
			g.groupID = i['groupID']
			#g.uID = i['uID']
			#0print '-----------', g.ID
			gr.append(g)

 		#%print '2. gr: ', gr
#2		return g
		return gr

	def selectWordsByGroupID(self,groupID):
		group_collection = DB.Group
		#0print 'gID: ',groupID
		a = group_collection.find({"_id": ObjectId(groupID)})


		#0print 'A:',a[0]
		g = None
 
		for i in a:
			g = GroupDataModel.Group()
			g.wordsID = i['wordsID']

		k = {}
		#0print g.wordsID
		k['_id'] = g.wordsID

		a = DB.Words.find({"_id":k['_id']})

		words = None

		for i in a:
			words = GroupDataModel.Words()
			words.queries = i['queries']
			words.keywords = i['keywords']
			words.ID = i['_id']

		return words


	def deleteGroup(self,group):
		group_collection = DB.Group
		a = group_collection.remove({"_id": ObjectId(group.ID)})
		return a['ok']

	def deleteWords(self,words):
		group_collection = DB.Words
		a = group_collection.remove({"_id": ObjectId(words.ID)})
		return a['ok']


	def insertGroup(self, groupSet):
#10		print groupSet
		i = 0
		groupID = groupSet.pop(0)
		cQueries = groupSet.pop(0)#.queries

		gresults = DB.Group.find({"cQueries":cQueries})

#10		print '00000000000'
#10		print gresults.count()

		if gresults.count() == 0:
			print 'Zero'
			for i in xrange(0,len(groupSet)):
				g = {}
				g['group_id'] = groupID
				g['cQueries'] = cQueries
				g['user_id'] = groupSet.pop(0)
				g['date'] = datetime.datetime.utcnow()

				DB.Group.insert(g)
		else:
			print 'existing'
			existings = []
			for gr in gresults:
				existings.append(gr)

			for i in xrange(0,len(groupSet)):
				isNewUser = 1
				guser = groupSet.pop(0)
				
				for existing in existings:
#1					print type(existing)
					groupID = existing['group_id']
#1					print existing['user_id'], ' ', guser, existing['user_id'] == guser
					if existing['user_id'] == guser:
						isNewUser = 0
						break

				if isNewUser == 1:
					g = {}
					g['group_id'] = groupID
					g['cQueries'] = cQueries
					g['user_id'] = guser
					g['date'] = datetime.datetime.utcnow()

					DB.Group.insert(g)

		#Load map and reduce functions
		map = Code(open('groupMap.js','r').read())
		reduce = Code(open('groupReduce.js','r').read())


		#Run the map-reduce query
		results = DB.Group.map_reduce(map,reduce,'resultss',query={'group_id' : groupID})

		#Print the results
		wordsSet = []
		words = None
		for result in results.find():
#1			print "result['_id']['group_id']"
#1			print result['_id']['group_id']
#1			print "result['_id']['queries']"
#1			print result['_id']['queries']
			words = GroupDataModel.Words()
			words.queries = result['_id']['queries']
			words.group_id = result['_id']['group_id']
#			words.keywords = i['keywords']
#			words.ID = i['_id']
			wordsSet.append(words)

#10		print '-----------------------------\nwordsSet'
#10		print wordsSet
		return wordsSet		



