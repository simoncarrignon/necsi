testimpA=read.csv("../../../dev/trieste-lens/data/final_table_dist-import.csv")
testexpA=read.csv("../../../dev/trieste-lens/data/final_table_dist-export.csv")
for(year in sort(unique(testimpA$year))){
testimp=testimpA[testimpA$year == year,]
testexp=testexpA[testimpA$year == year,]

png(paste0("indus",year,".png"),width=1200,height=800)
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
