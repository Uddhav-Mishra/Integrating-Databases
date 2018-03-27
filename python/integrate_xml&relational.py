import xml.etree.ElementTree as ET
import lxml.etree as LE
import pymysql
import sys
import re



"""
WORKING

doc=LE.parse("book_details.xml")
x = doc.xpath('//bookname[text()="dsd"]')
print(x[0].text,x[1].tag)

doc=LE.parse("book_details.xml")
x = doc.xpath('book/bookname[text()="dsd"]/parent::book/cost')
print(x[0].text,x[1].text)
 
"""


# q  = 'book/price[text()<=34]/parent::book/title'
zz  = 'book/price[text()<=34]/parent::book/title\n'
q=input(("input xpath query relative to dtd provided\n sample xpath query is given for reference:\n"+zz))
s=''
tokens=[] 
for i in range(0,len(q)):
    if (q[i]=='/' or q[i]==':'):
       if(len(s)>0):
           tokens.append(s)
           s=''
    elif (q[i]=='['):
        tokens.append(s)
        s=q[i];
    else:
        s+=q[i];
if(len(s)>0):
    tokens.append(s)
    s=''
    
search_author="uddhav"
#for i in range(0,len(tokens)):
#   print(tokens[i])
tree = ET.parse('tst.xml')
root = tree.getroot()
doc=LE.parse("book_details.xml")
for x in root.findall('book'):
    
    if (x.find('dbname').text=='null'):
       #print("FD")
       #print(x.find('filename').text)
       str='' ;
       for i in range(0,len(tokens)):
            if(i==0 or i==4):
                str+= (x.find('initialinf').text+'/')
            elif(i==1 or i==5):
                str+=(x.find(tokens[i]).text)
            elif(i==2):
                str+=(tokens[i]+'/')
            else:
                str+=(tokens[i]+'::')
            
       #str = x.find('initialinf').text+'/'+x.find('author').text+ '[text()="'+search_author+'"]/parent::'+x.find('initialinf').text+'/'+x.find('title').text
       #print(str)
       y=doc.xpath(str)
       for z in range(0,len(y)):
           print(y[z].text);


    else:
        conn = pymysql.connect(host='localhost', port=3306, user='root',
        passwd='1234', db=x.find('dbname').text, charset='utf8mb4', autocommit=True)
        sd=''
        flag=0;
        for i in range(0,(len(tokens[2])-1)):
            if flag==1:
                sd+=tokens[2][i]
            if (tokens[2][i]==')'):
                flag=1
        #print(sd)
        str = "select "+x.find(tokens[5]).text+" from "+x.find('tbname').text+" where "+x.find(tokens[1]).text+sd
        #print(str)
        cur=conn.cursor()
        cur.execute(str)
        for row in cur:
            print(row)
        cur.close()
        conn.close()
        

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



