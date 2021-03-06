import model
import dbmanager


from dbmanager import DBManager
from model import User
from model import GroupDataModel

if __name__ == "__main__":
    print "DB Manager Test File\n"
    print "Testing Database Access Operation (User Table)"

    d = DBManager.DBManager()

    print "Creating Group..."
    words = GroupDataModel.Words()
    group = GroupDataModel.Group()

    words.queries = ['python','sorted']
    words.keywords = []

    group.words = words
    d.createGroup(group)
    
    print "Selecting Group...."

    queries = ['python','sorted']
    if d.groupExistsByQueries(queries) == True:
        print "YES"

    print "Done"
    
    
