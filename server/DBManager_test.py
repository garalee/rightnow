import model
import dbmanager


from dbmanager import DBManager
from model import User

if __name__ == "__main__":
    print "DB Manager Test File"

    d = DBManager.DBManager()

    user = User.User(0,0,'abcd')
    d.deleteUser(user)
