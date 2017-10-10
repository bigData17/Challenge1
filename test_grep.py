import os 

for i in range(1,100):
	os.system('egrep -o  "kitten.{15,85}cat.{0,100}sire.{0,200}oxford" cats.txt')
	os.system('egrep -o  "english.{0,200}cat" cats.txt')
	os.system('egrep -o  "china.{30,150}cat" washington.txt')
	os.system('egrep -o  "cat.{0,100}anatomy" washington.txt')
	os.system('egrep -o  "cat.{0,10}are.{0,10}to" cats.txt')