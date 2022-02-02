#!/usr/bin/env python

test = "test.txt"

f = file(test)
c = f.readlines()

while True:

 user_input = raw_input("\033[32;1muser:\033[0m").strip()
 if len(user_input) == 0 : print "empty input!" ; continue
 for line in c:
   if user_input in line:
		print line
		break
 else:
	print "\033[31;1mmuyou!\033[0m"


