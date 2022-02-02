#!/usr/bin/env python

this = 2014
name = raw_input("name:")
age = int(raw_input("age:"))
sex = raw_input("sex:")
dep = raw_input("dep:")

msg = '''info:
	name:%s
	age:%d
	sex:%s
	dep:%s
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
