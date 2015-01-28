import xml.sax
import xml.sax.xmlreader
import xml.sax.saxutils
import sys

import dbconfig

# **************************************************
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
# *************************************************


class DictionaryHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.wordToId = {}
        self.idToWord = {}
    
    def startElement(self,tag,attributes):
        self.CurrentData = tag
       

        if tag == "Map": 
            self.id = None
            self.word = None


    def endElement(self,tag):
        if tag == "Map":
            if (not self.id == None) and (not self.word == None):
                self.wordToId[self.word] = self.id
                self.idToWord[self.id] = self.word

        self.CurrentData = ""

    
    def characters(self,content):
        if self.CurrentData == "ID":
            self.id = content

        if self.CurrentData == "Word":
            self.word = content

    def parse(self,f):
        xml.sax.parse(f,self)
        return (self.idToWord, self.wordToId)


    def save(self,fname,idToWord,wordToId):
        f = open(fname,'w')
        x = xml.sax.saxutils.XMLGenerator(f,'utf-8')
        attr0 = xml.sax.xmlreader.AttributesImpl({})

        x.startDocument()
        x.startElement("Dictionary", attr0)

        for key in wordToId.keys():
            digit = wordToId[key]
            x.startElement("Map",attr0)

            x.startElement("ID",attr0)
            x.characters(digit)
            x.endElement("ID")

            x.startElement("Word",attr0)
            x.characters(key)
            x.endElement("Word")

            x.endElement("Map")

        x.endElement("Dictionary")
        x.endDocument()
        

a,b =  DictionaryHandler().parse(dbconfig.dictionaryfile)
DictionaryHandler().save("TEST.xml",a,b)
