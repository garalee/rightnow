import model
import dbmanager


from dbmanager import DBManager
from model import User

if __name__ == "__main__":
    print "DB Manager Test File\n"
    print "Testing Database Access Operation (User Table)"

    d = DBManager.DBManager()

    print "Creating a New User...."
    user = User.User(facebookID="abcdttt",passwd="rightnow")
    userID = d.createUser(user)
    print "Done... ID of the User is", userID
    print ""

    print "finding a User..."
    user = d.findUserByID(userID)
    print "Done... profile of the user :"
    print user
    print ""

    print "Deleting a User..."
    d.deleteUser(user)
    print "Done"
