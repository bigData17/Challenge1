# inp = ['endnu' , 'en' , 'test']

# se = set(inp)

# def ouch(a):
# 	r = []
# 	with open('linesets_astext.txt', 'r') as s:
# 		for i, b in enumerate(s):
# 				b_s = set(b.split())
# 				c = a & b_s
# 				if(c==a):
# 					print c
# 					print i 
# 					r.append(i)
# 	return r

# liste = ouch(se)

# with open('wiki_astext.txt', 'r') as lines:
# 	with open('output_lines.txt', 'w') as output:
# 		for i,b in enumerate(lines):
# 			if (i in liste):
# 				output.write(b)
# output.close()
# lines.close()


import os 
# os.system('egrep -o  "endnu[[:blank:][:alpha:]*]{5,15}en[[:blank:][:alpha:]*]{0,20}test" output_lines.txt')

#    ['kitten', (15, 85), 'cat', (0, 100), 'sire', (0, 200), 'oxford']

for i in range(1,100):
	os.system('egrep -o  "kitten.{15,85}cat.{0,100}sire.{0,200}oxford" cats.txt')
	os.system('egrep -o  "english.{0,200}cat" cats.txt')
	os.system('egrep -o  "china.{30,150}cat" washington.txt')
	os.system('egrep -o  "cat.{0,100}anatomy" washington.txt')
	os.system('egrep -o  "cat.{0,10}are.{0,10}to" cats.txt')