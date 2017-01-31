f = open("Dimensions.csv","r")
ftemp = open("Dimensions_clean.csv","w")
#ftemp = open("temp.csv","w") 
open_flag = False
while True:
	c = f.read(1)
	#print(c)
	if not c:
		break
	elif c=='"':
		open_flag=False if open_flag==True else True
		print(open_flag)
		ftemp.write(c)
	elif c=="\n" and open_flag==True:
		ftemp.write(" ")
	else:
		ftemp.write(c)
f.close()
ftemp.close()
