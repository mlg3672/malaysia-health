# web scraping malaysia doe air quality 
library(XML)
library(RCurl)

setwd("~/Documents/R reference")

url <-"http://apims.doe.gov.my/v2/hourly2.php"
webpage<-getURL(url)
webpage <- readLines(tc <- textConnection(webpage)); close(tc)

#creates a list 
tables<- readHTMLTable(url)

#convert list to data frame
newtab<-data.frame(t(sapply(tables,c)))
try<-do.call(rbind, lapply(tables, data.frame, stringsAsFactors=FALSE))

#change column names
colnames(newtab) <- c("State", "Area","TIME6.00AM","TIME7:00AM","TIME8.00AM","TIME9.00AM","TIME10.00AM","TIME11.00AM")

#remove special character, change columns to numeric
x <- "~!@#$%^&*" 
str_replace_all(x, as.character(try[,3:8]), " ")
as.numeric(newtab[,3:8])
dat<-do.call(rbind, lapply(tables, data.frame, stringsAsFactors=FALSE))
dat[, -(1:2)] <- sapply(dat[, -(1:2)], function(col) {
  as.numeric(sub("[*]$", "", col))
  })
#repalce NAs
try[try=="n/a"]<-NA

#find column means
colMeans(dat[,c("MASA.TIME09.00AM","MASA.TIME10.00AM","MASA.TIME11.00AM")],na.rm=T)

#add a date column

#add time column and aqi column
library(reshape2)
hav<--melt(dat)

#change time column
hav[,3]<-gsub("[MASSA.TIME]","",hav[,3])
hav[,3]<-gsub('^([0-9]{1,2})([0-9]{2})$', '\\1:\\2', hav[,3])
hav[,3]<-strptime(hav[,3],"%R") ##TROUBLE

#boxplot by state, area, time
boxplot(dat$MASA.TIME06.00AM,col="blue")
boxplot(MASA.TIME06.00AM ~ NEGERI...STATE,data=dat,col="red")
boxplot(KAWASAN.AREA~ value,data=hav,col="red")

#histogram
hist(dat$MASA.TIME06.00AM,col="green",breaks=10)
rug(dat$MASA.TIME06.00AM)
abline(v=150,lwd=2)

#scatterplot
with(dat,plot(MASA.TIME06.00AM,NEGERI...STATE,col=KAWASAN.AREA,main="pm 10 by state"))

#loop get all historical data<---LAST STEP
url=http://apims.doe.gov.my/v2/hourly1.php?date=2015-04-18


#save
write(tables,"aqi1.csv",sep="\n")
date<-date()
writeLines(text=c(date),"aqi1.csv")
read.csv("aqi1.csv")
gsub("\\n*",".")
    