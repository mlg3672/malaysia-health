def getpages(url,url2,day,time):
    '''
    url and url2 are strings of base webaddress
    day is a list of strings that is between url and url2
    time is a list of strings that appends to url2
    '''
    for i in day:
        for j in time:
            nurl = url + j + url2 + i
            print(nurl)
            #nfile = readHTMLtable(nurl)
            print('data/'+i+'aqi'+j+'.csv')

#test function
url ='http://apims.doe.gov.my/v2/hourly'
url2 = '.php?date='
time = ['1','2','3','4']
day = ['2015-04-18','2015-04-17','2015-04-16']
getpages(url,url2,day,time)