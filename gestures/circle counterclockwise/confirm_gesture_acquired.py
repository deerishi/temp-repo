f1x=open('trial_circlex4.txt','r')
f1y=open('trial_circley4.txt','r')
f1z=open('trial_circlez4.txt','r')

f2x=open('circle_counterclockwise_x','a')
f2y=open('circle_counterclockwise_y','a')
f2z=open('circle_counterclockwise_z','a')

for line in f1x:
	f2x.write(line)

for line in f1y:
	f2y.write(line)

for line in f1z:
	f2z.write(line)

