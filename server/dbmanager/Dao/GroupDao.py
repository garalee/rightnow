from dbmanager.Dao import DB
from model import GroupDataModel

class GroupDao:
    def insertWords(self,words):
        words_collection = DB.Words

        w = {}
        w['keywords'] = words.keywords
        w['queries'] = words.queries

        return DB.Words.insert(w)

    def insertGroup(self,group):
        group_collection = DB.Group
        words_collection = DB.Words

        wordsID = self.insertWords(group.words)
        g = {}
        g['wordsID'] = wordsID

        return group_collection.insert(g)
        
    def selectWordsByQueries(self,queries):
        words_collection = DB.Words

        w = {}
        w['queries'] = queries

        a = DB.Words.find(w)
        words = GroupDataModel.Words()

        for i in a:
            words.queries = i['queries']
            words.keywords = i['keywords']
            words.ID = i['_id']

        return words
        

    def selectWordsByKeywords(self,keywords):
        words_collection = DB.Words
        
        k = {}
        k['keywords'] = keywords
        
        a = DB.Words.find(k)
        words = GroupDataModel.Words()
        
        for i in a:
            words.queries = i['queries']
            words.keywords = i['keywords']
            words.ID = i['_id']
            
        return words
        

    def selectWordsByQueriesAndKeywords(self,queries,keywords):
        words_collection = DB.Words

        w = {}
        w['queries'] = queries
        w['keywords'] = keywords

        a = DB.Words.find(w)
        words = GroupDataModel.Words()

        for i in a:
            words.queries = i['queries']
            words.keywords = i['keywords']
            words.ID = i['_id']

        return words


    def selectGroupByQuery(self,query):
        pass
    
    def selectGroupByID(self,groupID):
        group_collection = DB.Group
        wordss_collection = DB.Words

        a = group_collection.find({"_id":groupID})

        g = GroupDataModel.Group()
        
        for i in a:
            g.ID = i['_id']


    def updateGroup(self,groupID):
        pass
