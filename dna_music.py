import winsound
import os

aList = [];

f = open(r'DNA.txt')
num_lines = sum(1 for line in 'DNA.txt')

print num_lines

for i in range(num_lines):
         #print str(i) + ': ' + f.readline(),
         #print f.readline(),
	#test[i]= f.readline()

	aList.append( f.readline() );
	#print "Updated List : ", aList;
	
f.close()

#print "List : ", aList;
print("------------DNA LINES------------")
print("")

for k in range(0, num_lines):
	print "LINE",k+1, aList[k];
print("")
print("")


#Morse Code-ish
for x in range(0, num_lines):
	for i in aList[x]:
    		if i == 'C':winsound.Beep(700,1000) 
    		if i == 'A':winsound.Beep(600,500) 
    		if i == 'T':winsound.Beep(500,300) 
    		if i == 'G':winsound.Beep(250,1000) 
		print "line" , x+1, "CODE", i




print("")
wait = input("PRESS ENTER TO CONTINUE.")
