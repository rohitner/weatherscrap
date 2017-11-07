data = read.csv(file="edmonton.csv", header=FALSE, sep=",")
colnames(data)=NULL
plot(data[,6])
plot(data[,3])
