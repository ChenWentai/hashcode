import sys

import string

#------------class pizza---------------
class Pizza:
 def __init__(self,pizza):
   self.raw = pizza
   self.size = len(self.raw)*len(self.raw[0])
   self.split = []
   self.splitted = []
   self.num_T = []
   self.num_M = []
   #self.split = [[] for x in range(self.size)]
   #self.splitted = [[] for x in range(self.size)]
   self.result = []
   self.check = []
  
 def print_pizza(self):
   print self.raw

#------split function--------
def split(slices,pattern):
  row = len(slices.raw)
  colomn = len(slices.raw[0])
##  #print "row:",row,"colomn:",colomn
  r1=r2=c1=c2=0
  width = length = 0
## print "raw1:",slices.raw
  for i in range(len(pattern)):
    length = pattern[i][0]
    width = pattern[i][1]
##  print "length:",length,"width:",width
    for r1 in range(row):
	      r2 = r1 + length-1
	      if r2 >= row:
        	 break
	      for c1 in range(colomn):
        	c2 = c1 + width -1
		if c2 >= colomn:
		  break
		current = [r1,c1,r2,c2]
##		print "current_avant:",current
		if not overlap2(slices,r1,c1,r2,c2):		
	        #if not overlap(slices.split,current):
		  #print "current split:",slices.split
		  #print "current_not_overlap:",current
	        	slices.split.append([r1,c1,r2,c2])       
##		        print "------------------bingo!-----------------"
			for i in range(r1,r2+1):
			  for j in range(c1,c2+1):
				slices.check[i][j] = '-1'
	
			#	print "check:",slices.check[i][j]
			#temp = list(slices.check[i][j])
			#temp
#------combination-------
#def combination(pizza,split):
# for i 
#--------NEW-overlap----------
def overlap2(test,r1,c1,r2,c2):
  ##print (r1,c1,r2,c2)
  for i in range(r1,r2+1):
    ##print "check[i]",test.check[i][c1:c2+1]
    if ('-1' in test.check[i][c1:c2+1]):
	return True
  return False
#-------pattern function-------
def create_pattern(size):
	pattern = []
	for i in range(1,size+1):
		if size%i == 0:
			pattern.append([i,size/i])
	return pattern


#--------------
# overlap function

def overlap(result,current_slice):
  r = result
  c = current_slice
  current = []
  result = []
  for i in range(c[0],c[2]+1):
	for j in range(c[1],c[3]+1):
		#print "i:",i,"j:",j
		current.append([i,j])
  #print "current:",current
  for i in range(len(r)):
	for j in range(r[i][0],r[i][2]+1):
		for k in range(r[i][1],r[i][3]+1):
			result.append([j,k])
  for i in current:
    if i in result:
	return True
  return False
		
#------------------splitted function-----------------

def splitted(pizza):
 num_slice = len(pizza.split)
 #print "num_slice:",num_slice
 #print "split:",test.split
 for i in range(num_slice):
  pizza.splitted.append([])
  for j in range(pizza.split[i][0],pizza.split[i][2]+1):
   for k in range(pizza.split[i][1],pizza.split[i][3]+1):
    pizza.splitted[i].append(pizza.raw[j][k])
   # print "splitted:",pizza.splitted
 return 0

#-------------check function------------------

def check(slices,L,H):
 for i in range(len(slices.num_T)):
  if slices.num_T[i] >= L and slices.num_M[i] >= L and (slices.num_T[i]+slices.num_M[i]) <= H:
   slices.result.append(slices.split[i]) 
 
#---------------CALCULATE NUMBER--------------

def calculate_num(slices):
  slices.num_T = []
  slices.num_M = []
  for i in range(len(slices.splitted)):
    slices.num_T.append(0)
    slices.num_M.append(0)
    for j in range(len(slices.splitted[i])):
     if slices.splitted[i][j] == 'T':
       slices.num_T[i]= slices.num_T[i] + 1
     if slices.splitted[i][j] == 'M':
       slices.num_M[i] = slices.num_M[i] + 1

  #return [num_T,num_M]

#-------read data--------

data = sys.argv[1]
grid = open(data,'r').read()
grid = grid.split('\n')
#print "grid:",grid
pizza = []
para = grid[0].split(' ')
total_size = int(para[0])*int(para[1])
L = int(para[2])
H = int(para[3])
#print "para:",para
#print "L:",L,"H:",H
#print "para:",para
for i in range(1,len(grid)):
    	pizza.append(grid[i])
pizza = filter(None,pizza)
for i in range(len(pizza)):
 pizza[i] = list(pizza[i])

test = Pizza(pizza)
for i in range(len(test.raw)):
    test.check.append([])
    for j in test.raw[i]:
        test.check[i].append(j)
##print "check:",test.check
#print "raw:"
#test.print_pizza()
#print type(test.raw)
#test.raw[0][0] ='3'
#result = []

max_size = H
p = []
for i in range(L*2,max_size):
	p.append(create_pattern(i))

p2 = []
for i in p:
	for j in i:
		p2.append(j)
##print "pattern:",p2
#p2.reverse()
##print "reverse pattern:",p2
#for i in range(len(p2)):
split(test,p2)
##print "split:",test.split
##print "raw:",test.raw
##print "check:",test.check
splitted(test)
#print "splitted:",test.splitted
##print "len(splitted):",len(test.splitted)
calculate_num(test)
##print test.num_T,test.num_M 
check(test,L,H)
##print "result length:",len(test.result)
##print "result:",test.result
number = 0
for i in range(len(test.result)):
	number = number + len(test.result[i])	
##print "number:",number
final_result = []
print len(test.result)
#print "result:",test.result

final = str(len(test.result))
final+='\n'
for i in range(len(test.result)):
 final_result.append(map(str,test.result[i]))
 final+=' '.join(final_result[i])
 final+='\n'
print "final:"
print final
f = open('out_example.txt','w')
print >> f, final
#print len(test.result)
