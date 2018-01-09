testimpA=read.csv("data/final_table_dist-import.csv")
testexpA=read.csv("data/final_table_dist-export.csv")
for(year in sort(unique(testimpA$year))){
testimp=testimpA[testimpA$year == year,]
testexp=testexpA[testimpA$year == year,]

png(paste0("images/indus",year,".png"),width=1200,height=800)
par(mfrow=c(1,2))
type=tapply(testimp$boat , testimp[,c("port","type")], sum)
type
plot( type[,1] ~ type[,2],ylab="steamboat",xlab="vessel",main="import",log="xy",ylim=c(1,10000),xlim=c(1,10000))
text(type[,2] , type[,1], rownames(type),ylab="steamboat",xlab="vessel",main="export",ylim=c(1,10000),xlim=c(1,10000))
lines(1:10000,1:10000)
mtext(year)

type=tapply(testexp$boat , testexp[,c("port","type")], sum)
plot( type[,1] ~ type[,2],ylab="steamboat",xlab="vessel",main="export",log="xy",ylim=c(1,10000),xlim=c(1,10000))

text(type[,2] , type[,1], rownames(type),ylab="steamboat",xlab="vessel",main="export",ylim=c(1,10000),xlim=c(1,10000))
lines(1:1000000,1:1000000)
mtext(year)
dev.off()
}

#analysis of the RATIO only
#aggregateallyears:
testimp=read.csv("data/final_table_dist-import.csv")
testexp=read.csv("data/final_table_dist-export.csv")
png("images/totalRatio.png",width=1500,height=800)
par(mfrow=c(1,2),mar=c(8,5,1,1))
type=tapply(testimp$boat , testimp[,c("port","type")], sum)
type[is.na(type)]=1 #if there is NA it means that there were no boat of this type. But as we need a ratio we cannot divide by 0 so NA=1
rttype=type[,1]/type[,2]
plot(sort(rttype),axes=F,log="y",ylab="ratio steam/vessel",xlab="",main="import") 
axis(2)
axis(1,labels=names(sort(rttype)),at=1:length(sort(rttype)),las=3,cex=.5)

type=tapply(testexp$boat , testexp[,c("port","type")], sum)

type[is.na(type)]=1 #if there is NA it means that there were no boat of this type. But as we need a ratio we cannot divide by 0 so NA=1
rttype=type[,1]/type[,2]
plot(sort(rttype),axes=F,log="y",ylab="ratio steam/vessel",xlab="",main="export") 
axis(2)
axis(1,labels=names(sort(rttype)),at=1:length(sort(rttype)),las=3)
dev.off()





for(year in sort(unique(testimpA$year))){
testimp=testimpA[testimpA$year == year,]
testexp=testexpA[testimpA$year == year,]

png(paste0("images/indus",year,".png"),width=1200,height=800)
par(mfrow=c(1,2))
type=tapply(testimp$boat , testimp[,c("port","type")], sum)
rttype=type[,1]/type[,2]
plot( type[,1] ~ type[,2],ylab="steamboat",xlab="vessel",main="import",log="xy",ylim=c(1,10000),xlim=c(1,10000))
text(type[,2] , type[,1], rownames(type),ylab="steamboat",xlab="vessel",main="export",ylim=c(1,10000),xlim=c(1,10000))
lines(1:10000,1:10000)
mtext(year)

type=tapply(testexp$boat , testexp[,c("port","type")], sum)
plot( type[,1] ~ type[,2],ylab="steamboat",xlab="vessel",main="export",log="xy",ylim=c(1,10000),xlim=c(1,10000))

text(type[,2] , type[,1], rownames(type),ylab="steamboat",xlab="vessel",main="export",ylim=c(1,10000),xlim=c(1,10000))
lines(1:1000000,1:1000000)
mtext(year)
dev.off()
}
