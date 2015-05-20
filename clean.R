# web scraping malaysia doe air quality 
library(XML)
library(RCurl)
library(stringr)
library(reshape2)
library(lubridate)

#setwd("Documents/R-Projects/malaysia-health")

url <-"http://apims.doe.gov.my/v2/hourly2.php"

# extracts table data
tables<- readHTMLTable(url)

# remove special character, change columns to numeric
dat<-do.call(rbind, lapply(tables, data.frame, stringsAsFactors=FALSE))
dat[, -(1:2)] <- sapply(dat[, -(1:2)], function(col) {
  as.numeric(sub("[*]$", "", col))
  })
  
# reformat data
hav<-melt(dat)

# reformat time column
hav[,3]<-gsub("[MASSA.TIME]","",hav[,3])
hav[,3]<-substr(as.POSIXct(sprintf("%04.0f", as.numeric(hav[,3])), format='%H%M')
,12,16)
hav[,3]<-as.factor(hav[,3])

# change column names
colnames(hav) <- c("state", "area","time","AQI")

# add date column
hav$ymd<-substring(Sys.time(),1,10)

#save data file
save(hav,file=paste(1,"_","aqi", Sys.Date(), ".csv", sep = ""))