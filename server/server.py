import model
import dbmanager

from dbmanager import DBManager
from model import User


if __name__ == "__main__":
    print "DB MANAGER TEST"

    d = DBManager.DBManager()
    print d.selectUser(0)
