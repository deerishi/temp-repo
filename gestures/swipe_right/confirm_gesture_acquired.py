f1x=open('trial_swipe_right_x.txt','r')
f1y=open('trial_swipe_right_y.txt','r')
f1z=open('trial_swipe_right_z.txt','r')

f2x=open('swipe_rightx','a')
f2y=open('swipe_righty','a')
f2z=open('swipe_rightz','a')

for line in f1x:
	f2x.write(line)

for line in f1y:
	f2y.write(line)

for line in f1z:
	f2z.write(line)

