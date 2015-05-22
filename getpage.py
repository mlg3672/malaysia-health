from lxml import etree, html
from lxml.html import parse
import numpy

def getpages(url,url2,day,time):
    '''
    This function gets a HTML table from url
    url and url2 are strings of base webaddress
    day is a list of strings that is between url and url2
    time is a list of strings that appends to url2
    '''
    for i in day:
        for j in time:
            nurl = url + j + url2 + i
            htmltree = html.parse(nurl)
            filename = str(i)+'aqi'+str(j)+'.txt'
            file = open("data/"+filename, "w")
            file.write(str(etree.tostring(htmltree, pretty_print=True)))
            file.close()

def htmltab(path):
    '''
    path is a string of a text (html) file in local directory
    url is a string, web address
    '''
    page = parse(path)
    #page = html.parse(url)
    rows = page.xpath("//tr")
    data = list()
    for row in rows:
        data.append([c.text_content() for c in row.getchildren()])
    return data   

def removechar(dat,char,convert=True):
    '''
    dat is a list of string values to be converted to table
    char is special character to remove
    convert is a binary whether to convert to numerical
    '''
    #method #1 Works BUT changes to long list 
    a = [(b.replace(char,'')) 
        for i, c in enumerate(dat)
        for b in c]
    a = [replace_NAs(x) for x in a]
    if convert == True:
        a = [float(i) for i in a]
    #method #2 FAIL
    ar = numpy.array(dat)
    pos = numpy.char.find(ar,char)
    for elem in ar:
        elem = [(i.replace(char,'')) for i in elem if char in i]
    #problem only returns elements replaced
    
def replace_NAs(rows,NA_values=["n/a"]):
    for x in rows:
        if x in NA_values:
            return 'NA'
        else:
            return x

 
    
#test functions
url ='http://apims.doe.gov.my/v2/hourly'
url2 = '.php?date='
time = ['1','2','3','4']
day = ['2015-04-19','2015-04-17','2015-04-16']
path = "Documents/R-Projects/malaysia-health/data/2015-04-19aqi1.txt"
getpages(url,url2,day,time)
data = htmltab(path)
removechar(data,'*',True)