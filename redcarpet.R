setwd("D:/redcarpet")
rm(list=ls())
sec<- read.csv(file.choose())
str(sec)
library(lubridate)
#here i'm coverting the date format to ymd.
sec$Date<- ymd(sec$Date)
library(jsonlite)
#json file is being imported
json_file<- fromJSON("http://doppler.finra.org/doppler-lookup/api/v1/search/firms?hl=true&nrows=99000&query=Blackstone&r=2500&wt=json")
summary(json_file)
library(dplyr)
install.packages("rjson")
library(rjson)
install.packages("plyr")
library(plyr)
#here i'm coverting json file to dataframe
json<- data.frame(number = unlist(json_file))
#here i'm fetching names of the firms from the json file in  newly created json_data.
json_data<- json$number[99:122]
#here i'm converting json_data to a data frame.
json_data<- as.data.frame(json_data)
#here i'm adding the fetched id from the json to json_data.
json_data$id<- json$number[75:98]
#here i'm writing the json data in csv format.
write.csv(json_data, file = "json_data.csv")

