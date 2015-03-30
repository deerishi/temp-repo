f1x=open('trial_squarex.txt','r')
f1y=open('trial_squarey.txt','r')
f1z=open('trial_squarez.txt','r')

f2x=open('squarex.txt','a')
f2y=open('squarey.txt','a')
f2z=open('squarez.txt','a')

for line in f1x:
	f2x.write(line)

for line in f1y:
	f2y.write(line)

for line in f1z:
	f2z.write(line)

