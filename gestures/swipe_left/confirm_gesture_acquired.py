f1x=open('trial_swipe_left_x.txt','r')
f1y=open('trial_swipe_left_y.txt','r')
f1z=open('trial_swipe_left_z.txt','r')

f2x=open('swipe_leftx','a')
f2y=open('swipe_lefty','a')
f2z=open('swipe_leftz','a')

for line in f1x:
	f2x.write(line)

for line in f1y:
	f2y.write(line)

for line in f1z:
	f2z.write(line)

