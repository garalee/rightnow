import xml.sax
import xml.sax.xmlreader
import xml.sax.saxutils

f = open('qqq.xml','w')

x = xml.sax.saxutils.XMLGenerator(f,'utf-8')
attr0 = xml.sax.xmlreader.AttributesImpl({})

x.startDocument()
x.startElement("Test",attr0)

x.startElement("Map",attr0)
x.characters("1 ")
x.characters("2 ")
x.characters("3")
x.endElement("Map")

x.endElement("Test")

x.endDocument()


