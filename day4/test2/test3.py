#!/usr/bin/env python

#wolf test

test = "test.txt"

f = file(test)
c = f.readlines()

while True:
  user = raw_input("\033[32;1minput user:\033[0m")
  if user == "wolf" :
    p = raw_input("\033[32;1minput pass:\033[0m")
    ps = "1234"
    while p != ps :
      p = raw_input("\033[31;1mcuowu pass:\033[0m")
    else :
      print "\033[31;1mOK!~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m"

      while True:
        user_input = raw_input("\033[32;1muser:\033[0m").strip()
        if len(user_input) == 0 :print "empty input!";continue
        for line in c:
          if user_input in line:
		print line
		break
        else:
        	print "\033[31;1mmuyou!\033[0m"


