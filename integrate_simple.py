import xml.etree.ElementTree as ET
import lxml.etree as LE
import pymysql
import sys
import re

"""
WORKING
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='book_manager', charset='utf8mb4', autocommit=True)
str = "select * from books"
cur=conn.cursor()
cur.execute(str)
for i in range(0,len(cur.description)):
	print(cur.description[i][0],end=" ")
print()
for row in cur:
    print(row)
cur.close()
conn.close()"""

"""
WORKING

doc=LE.parse("book_details.xml")
x = doc.xpath('//bookname[text()="dsd"]')
print(x[0].text,x[1].tag)

doc=LE.parse("book_details.xml")
x = doc.xpath('book/bookname[text()="dsd"]/parent::book/cost')
print(x[0].text,x[1].text)
 
"""
# names of books with author name y
query_string = 'book/author[text()="uddhav"]/parent::book/price'
search_author="uddhav"
tree = ET.parse('tst.xml')
root = tree.getroot()
doc=LE.parse("book_details.xml")
for x in root.findall('book'):
    
    if (x.find('dbname').text=='null'):
       #print("FD")
       print(x.find('filename').text)
       str = x.find('initialinf').text+'/'+x.find('author').text+'[text()="'+search_author+'"]/parent::'+x.find('initialinf').text+'/'+x.find('title').text
       #print(str)
       y=doc.xpath(str)
       for z in range(0,len(y)):
           print(y[z].text);


    else:
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db=x.find('dbname').text, charset='utf8mb4', autocommit=True)
        str = "select "+x.find('title').text+" from "+x.find('tbname').text+" where "+x.find('author').text+"='"+search_author+"'"
        #print(str)
        cur=conn.cursor()
        cur.execute(str)
        for row in cur:
            print(row)
        cur.close()
        conn.close()
        


"""
WORKING
tree = ET.parse('tst.xml')
root = tree.getroot()
y =  len(root) ;

for x in root.findall('book'):
    if (x.find('dbname').text=='null'):
        tree2=ET.parse(

for x in root.findall('book'):
    print(x.find('title').text)

"""

    

"""
fp = open("book_details.xml","r")
element = ET.parse(fp)
 
e = element.findall('data/book')
print(len(e))
for i in e:
    print(i.text)
"""
"""
tree = ET.parse('tst.xml')
root = tree.getroot()


x = root.findall("country")
print(x[0].get('name'))
if(root[0][0].text=="null"):print('gf')
"""



