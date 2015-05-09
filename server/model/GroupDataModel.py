
class Words:
	def __init__(self,ID=0,keywords=[],queries=[],user_id=None,group_id=None):
		self.ID = 0
		self.keywords = keywords
		self.queries = queries
		self.user_id = user_id
		self.group_id = group_id

class Group:
	def __init__(self,wordsID=None,words=None):
		self.ID = 0
		self.wordsID = wordsID
		self.words = words
