
class Words:
    def __init__(self,ID=0,keywords=[],queries=[]):
        self.ID = 0
        self.keywords = keywords
        self.queries = queries

class Group:
    def __init__(self,wordsID=None,words=None):
        self.ID = 0
        self.wordsID = wordsID
        self.words = words
