# Exercises for chapter 3:

# Name:Shishira Adiga

#3.1
'''def print_lyrics():
       print "I'm a lumberjack, and I'm okay."
       print "I sleep all night and I work all day."

    def repeat_lyrics():
    	print_lyrics()
    	print_lyrics()

    repeat_lyrics()'''

#3.1    
#NameError: 'repeat_lyrics' is not defined

#3.2
#I'm a lumberjack, and I'm okay.
#I sleep all night and I work all day.
#I'm a lumberjack, and I'm okay.
#I sleep all night and I work all day.
#question--how come you get the right answer?since you're calling function print_lyrics before defination.

#3.3
def right_justify(s):
	b=len(s)
	print(' '*(70-b)+s)

right_justify('time')

#3.4
#1
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)

#2
def do_twice(f,g):
	f(g)
	f(g)

def print_twice(s):
	print s*2

do_twice(print_twice,'start')

#3
def print_twice(s):
	print s*2

print_twice('start')

#4
def do_four(f,g):
	 do_twice(f,g)
	 do_twice(f,g)

def do_twice(f,g):
	f(g)
	f(g)

def print_twice(s):
	 print s*2
	 

do_four(print_twice,'start')
