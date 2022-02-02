#!/usr/bin/env python

#wolf test

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
         chadao = 0 
         user_input = raw_input("\033[32;1muser:\033[0m").strip()
         f = file("test.txt")        
         while True:
           c = f.readline()
           if len(user_input) == 0 :print "empty input!";break
           if len(c) == 0 : break
           if user_input in c:
                print "\033[31;1m%s\033[0m" %c        
	        chadao = 1
           else:           
                pass           
         if chadao == 0 :print "\033[31;1mmuyou!%s\033[0m" %user_input


