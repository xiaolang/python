#!/usr/bin/env python

#this = 2014
import sys

x = 0
n = "wolf"

while True:
    if x < 3 :	
	name: object = raw_input("name:").strip() #qu kong ge!
	if len(name) == 0 :
		print "empty name!"
		continue
	elif name == n :
        	print "you,%s!" %(name)
	else :
	        print "you sb!,%s ! "%(name)
                # x = x + 1 #ji shu
		x += 1	
		continue	
	break
    else :
	print "3+++++++"
	sys.exit()

age = int(raw_input("age:"))
sex = raw_input("sex:")
dep = raw_input("dep:")

msg = '''info:
	----------
	name:%s
	----------
	age:%d
	----------
	sex:%s
	----------
	dep:%s
	----------
	''' %(name, age, sex, dep)

print msg

if age < 20 :
	print "you < 20"
elif age == 20 :
	print "you = 20"
else :
	print "you > 20"

#print "hello",name,'\n'
#print "ni",age,"sui!","\n"
#print "chu sheng:",this - age
