#!/usr/bin/env python

#this = 2014
n = "wolf"
name = raw_input("name:").strip() #qu kong ge!
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

if name == n :
	print "you,wolf!"
else :
	print "you sb!"

#print "hello",name,'\n'
#print "ni",age,"sui!","\n"
#print "chu sheng:",this - age
