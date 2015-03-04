# -*- coding: utf-8 -*-

from dbmanager import MongoConnector

__all__ = ['GroupDao','UserDao','UserJoinDao','IPTableDao']


DB = MongoConnector.MongoConnector().getDatabase()

