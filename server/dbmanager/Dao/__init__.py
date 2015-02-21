# -*- coding: utf-8 -*-

from dbmanager import MongoConnector

__all__ = ['GroupDao','UserDao','UserJoinDao']


DB = MongoConnector.MongoConnector().getDatabase()

