#f = open("Objects.csv","r")
f = open("Objects_clean.csv","r")
'''count = 0
for line in f:
	count += 1
print(count)'''
header = f.readline()
header = header.strip().split(",")
print(header)
print(len(header))
#exit()
count = 0
for line in f:
	line1 = line.strip().split(",")
	if len(line1)!=15:
		print(line1)
		print(len(line1))
		print(line)
		print(count)
		#exit()
		print("---------------------------------------------------------------")
	count += 1
	if (count==10):
		exit()
