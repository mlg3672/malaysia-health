from lxml import etree, html
from lxml.html import parse

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
    rows = page.xpath("//tr/td")
    data = list()
    for row in rows:
        data.append([c.text_content() for c in row.getchildren()])
    return data   
    
#test functions
url ='http://apims.doe.gov.my/v2/hourly'
url2 = '.php?date='
time = ['1','2','3','4']
day = ['2015-04-19','2015-04-17','2015-04-16']
path = "Documents/R-Projects/malaysia-health/data/2015-04-19aqi1.txt"
getpages(url,url2,day,time)
htmltab(path)