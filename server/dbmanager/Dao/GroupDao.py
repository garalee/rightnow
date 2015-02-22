from dbmanager.Dao import DB
from model import GroupDataModel

class GroupDao:
    def insertWords(self,words):
        words_collection = DB.Words

        w = {}
        w['keywords'] = sorted(words.keywords)
        w['queries'] = sorted(words.queries)

        return DB.Words.insert(w)

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
    
    def selectGroupByID(self,groupID):
        group_collection = DB.Group
        a = group_collection.find({"_id":groupID})

        
        g = None
 
        for i in a:
            g = GroupDataModel.Group()
            g.ID = i['_id']
            g.wordsID = i['wordsID']

        return g


    def deleteGroup(self,group):
        group_collection = DB.Group
        a = group_collection.remove({"_id": group.ID})
        return a['ok']

    def deleteWords(self,words):
        group_collection = DB.Words
        a = group_collection.remove({"_id": words.ID})
        return a['ok']
