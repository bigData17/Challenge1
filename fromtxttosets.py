
with open('linesets_astext.txt', 'w') as s:
	with open('sets_astext.txt', 'w') as s1:
		with open('bigsets_astext.txt', 'w') as s2:
			with open('bigbigsets_astext.txt', 'w') as s3:
				with open("wiki_astext.txt", "rb") as f:
					i = 0
					lS = set()
					lM = set()
					lB = set()
					for line in f:
						i = i+1
						l1 = line.split()
						se = set(l1)
						for e in se:
							s.write(e)
							s.write(' ')
						s.write('\n')
						lS = lS|se
						if (i % 100==0 or i == 462712):
							lM = lM | lS
							for e in lS:
								s1.write(e)
								s1.write(' ')
							s1.write('\n')
							lS = set()
							if (i % 1000==0 or i == 462712):
								lB =lB | lM
								for e in lM:
									s2.write(e)
									s2.write(' ')
								s2.write('\n')
								lM = set()
								if (i % 10000==0 or i == 462712):
									for e in lB:
										s3.write(e)
										s3.write(' ')
									s3.write('\n')
									print i
									lB = set()





f.close()
s.close()
s1.close()
s2.close()
s3.close()





