f1x=open('gestures/trialx4.txt','r')
f1y=open('gestures/trialy4.txt','r')
f1z=open('gestures/trialz4.txt','r')

f2x=open('test/testx','a')
f2y=open('test/testy','a')
f2z=open('test/testz','a')

for line in f1x:
	f2x.write(line)

for line in f1y:
	f2y.write(line)

for line in f1z:
	f2z.write(line)

