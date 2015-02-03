f1x=open('trial_Zx4.txt','r')
f1y=open('trial_Zy4.txt','r')
f1z=open('trial_Zz4.txt','r')

f2x=open('Z_x','a')
f2y=open('Z_y','a')
f2z=open('Z_z','a')

for line in f1x:
	f2x.write(line)

for line in f1y:
	f2y.write(line)

for line in f1z:
	f2z.write(line)

