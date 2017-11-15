data = read.csv(file="edmonton.csv", header=FALSE, sep=",")
colnames(data)=NULL
plot(data[,1])
for (count in c(1:dim(data)[1]))
{
    lines(predict(smooth.spline(data[,count],spar=0.01),seq(1,length(data[,count]),len=1000)))
}
