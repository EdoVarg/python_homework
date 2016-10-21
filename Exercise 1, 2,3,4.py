#Exercise 1 =Homework1
#Try to answer the questions without running the code. Check your answers, 
#by running the code. You'll learn the most this way, by figuring things out, 
#instead of just running the code and reading off the answers. Hand in your answers!

# the code

my_str = '6.00x'

for char in my_str:

    print(char)

print('done')

#How many times is "6" printed out?
#1
#How many times is "." printed out?
#1
#How many times is "0" printed out?
#1
#How many times is "x" printed out?
#1
#How many times is "done" printed out?
#1

# the code

greeting = 'Hello!'

count = 0

for letter in greeting:

    count += 1

    if count % 2 == 0:

        print letter

    print letter

print 'done'


#How many times is H print out?
#1
#How many times is e print out? Disregard the letters in the word done.
#2
#How many times is l print out?
#3
#How many times is o print out? Disregard the letters in the word done.
#1
#How many times is ! print out?
#2
#How many times is done print out?
#1
# the code

school = 'uppsala'

num_vowels = 0

num_cons = 0

for char in school:

    if char == 'a' or char == 'e' or char == 'i'\

       or char == 'o' or char == 'u':

        num_vowels += 1

    elif char == 'u' or char == 'p':

        print char

    else:

        num_cons -= 1

print('num_vowels is: ' + str(num_vowels))

print('num_cons is: ' + str(num_cons))


#How many times is "p" printed out?
#0, invalid syntax
#How many times is "o" printed out?
#0, invalid syntax
#What will the value of the variable "num_vowels" be?
#0, invalid syntax
#What will the value of the variable "num_cons" be?
#0, invalid syntax


#Exercise 2 =Homework2
# 1 Opening/reading/writing files
#Along with the material for this first exercise you will find a 
#file named file1.txt. The script you should write has to open the file
#and create a new file containing the information formatted in this way:

import os 
os.chdir('/Users/VARG/Documents/Uppsala U/Doctorand/Courses/python/day 2/exercises/files')
f=open('file1.txt','r')

data=open('file1.txt','r')
liste=data.readlines()
data2=open('file2.txt','w')
i=1
for row in liste:
	print >> data2, "Entry ",i ," ",row
	i=i+1
data2.close()

liste=[] 
data=open('file1.txt','r')
for row in data: liste=liste+[row]

liste2=[]
i=1
for row in liste:
	liste2=liste2+["Entry ",str(i), " ",row]
	i=i+1

liststring=""
for row in liste2:
	liststring=liststring+row

data2=open('file2.txt','w')
data2.write(liststring)
for row in liste2: print row

data2.close()

#2 Filtering by line contents

#Along with the material for this second exercise there is a BED formatted file genome.bed,
#containing chromosome coordinates of intervals. Write a python script that ask the user to
#enter a chromosome name (e.g. chr20) and then opens and reads the BED file. The program
#must display all the lines from the file corresponding to the chosen chromosome name. A file is
#written containing the following information for the chosen chromosome:

def chromosome():
	chrnumber=raw_input("please indicate chromosome number")
	chromosome="chr"+chrnumber
	data=open('genome.bed','r')
	liste=data.readlines()
	request=[]
	for row in liste:
		if row.split()[0]==chromosome:
			request=request+[row]
	return request


#3 Parsing and data structures
#A file distance.dat is given. Each of its line contains the name of two cities and the distance
#between them; these quantities are separated by spaces or tabs. For instance one entry could
#be:
#New-York Boston 450
#Write a python program that parses this file and builds a data structure in memory to
#contain the result. It’s important to chose the right data structure for the task at hand. Would
#you use a list ? A tuple ? A list of lists ? A dictionary ? A set ? A tuple indexed dictionary ?
#A dictionary of dictionaries ?
#Using this data structure, compute the total distance of a given tour, specified in a tuple
#tour containing, in order, the names of the cities to visit. For instance, tour could be (“city1”,
#“city2”, “city3”, “city4”)

data=open('distance.dat','r')
liste=data.readlines()
dico={}
for row in liste:
	dico[row.split()[0]+"-"+row.split()[1]]=row.split()[2]
tour=["New-York","Geneva","Paris"]
dist=0
i=0
for city in tour:
	if i<len(tour)-1:
		if tour[i]+"-"+tour[i+1] in dico:
			dist=dist+int(dico[tour[i]+"-"+tour[i+1]])
		elif tour[i+1]+"-"+tour[i] in dico:
			dist=dist+int(dico[tour[i+1]+"-"+tour[i]])
	else:
		print dist
	i=i+1


#4 Functions and reusage
#4.0.1 A
#Write a python function called is_repetition() that takes two strings s1 and s2 as arguments
#and that returns true if s1 is solely composed of the motif s2 which can be repeated as many
#times as needed. For instance, s1 = “abcabcabcabc” is made of the repetition of the motif s2
#= “abc”, whereas s1 = “abcab” does not have any repeated motif, except itself.

def is_repetition(s1,s2):
	times= len(s1)/ len(s2)
	if s1== s2*times:
		return True
	else:
		return False

s1=="abcabcabcabcabc"
s2="abc"
print is_repetition(a,b)

#4.0.2 B
#Write a python function called find_motif(s1) that returns s2, the shortest motif that builds
#1. If s1 has no motif other than itself, the function returns s1.

def find_motif(s):

	motif=s[0:1]
	
	if s==motif*times:
		return motif
	return s
s3="abcabcabcabcabc"
print find_motif(s3)

#5 Combining files
#A collaborator gives you 3 different files. One with the chromosome names (chrom.txt), one
#with the start and end of fragments (start_end.txt) and one with the genes corresponding to
#it (gene.txt). Write a python script that will reconstruct one BED formatted file with these
#3 files. It would look like this:

column1=open('chrom.txt','r')
col1=column1.readlines()

column2=open('start_end.txt','r')
col2=column2.readlines()

column3=open('gene.txt','r')
col3=column3.readlines()

col1[0].split()[0]

final=open('final_file.txt','w')

i=0
for row in col1:
	print >> final, col1[i].split()[0]," ",col2[i].split()[0]," ",col2[i].split()[1]," ",col3[i].split()[0]
	i=i+1

final.close()

#Exercise 3 =Homework3

#The “Person” Class
#Modeling a person is a classic exercise for people who are trying to learn how
#to write classes. We are all familiar with characteristics and behaviors of
#people, so it is a good exercise to try.
#§ Define a Person(object) class.
#§ In the __init__(self) function, define several attributes of a person.
#Good attributes to consider are name, age, place of birth, and
#anything else you like to know about the people in your life.
#§ Write one method. This could be as simple
#as introduce_yourself(self). This method would print out a statement
#such as: "Hello, my name is Eric."
#§ Create a Person, set the attribute values appropriately, and print out
#information about the person.
#§ Call your method on the person you created. Make sure your
#method executed properly; if the method does not print anything
#out directly, print something before and after calling the method to
#make sure it did what it was supposed to.

#The “Person” Class
class Define_a_person(object):
	"""docstring for define_a_person"""
	def __init__(self,name, age, place_of_birth, sex, are_you_happy):
		self.name = name
		self.age = age
		self.place_of_birth = place_of_birth
		self.sex = sex
		self.are_you_happy = are_you_happy
	def Introduce_yourself(self):
		print "Hello, my name is", self.name, ". I am", self.age,"years old. I born in", self.place_of_birth,". I am a", self.sex, "and", self.are_you_happy, ", I am happy"
Javier= Define_a_person (name= "Javier", age=27, place_of_birth= "Colombia", sex="Male", are_you_happy="yes")
print Javier.Introduce_yourself()


#The “Sample” Class
#Modeling a sample is another classic exercise.
#§ Define a Sample(object) class.
#§ In the __init__(self) function, define several attributes of a sample.
#Some good attributes to consider are geographic coordinates (x,y),
#year), sample collector, or any other aspect of a sample you care to
#include in your class.
#§ Write one method. This could be something such
#as describe_sample(self). This method could print a series of
#statements that describe the sample, using the information that is
#stored in the attributes. Try to be creative.
#§ Create a Sample object, and use your method.
#§ Create several Sample objects with different values for the
#attributes. Use your method on several of your Sample.
#§ Use the file class_glossary.pdf and try to associate the following
#words with pieces of your code related to the sample class: Class,
#Attribute, Method, Instance, Instantation.
#§ Create a Child class that inherits from the class Sample, it could be
#a SkinSample, a SoilSample or a MoonSample for example. Also
#make an instance of that class.
#§ Make sure that your code then contains method that overrides a
#parent method.

#The “Sample” Class
	class Sample(object):
			"""docstring for define a sample"""
			def __init__(self, sample_name,collector,place, year):
				self.sample_name = sample_name
				self.collector = collector
				self.place = place
				self.year = year
			def describe_sample(self):
				if self.year<2009
				print "the sample are too ald"
				if self.place != upplands 
				print "the sample belongs to other experiment"
				if self.collector!= Javier
				print "the sample are not yours"
Sample1= describe_sample(sample_name=mp12,collector=Javier,place=upplands, year=2016)
Sample2= describe_sample(sample_name=mp6,collector=Javier,place=upplands, year=2015)
Sample3= describe_sample(sample_name=frog1,collector=Maria,place=upplands, year=2006)
Sample4= describe_sample(sample_name=mp1,collector=Javier,place=Colombia, year=2013)
Sample5= describe_sample(sample_name=mp4,collector=Javier,place=upplands, year=2000)

#Rewrite the script presented in the file pythoninstyle_exerciseA.py (folder
#day_03/code).
#Try to avoid redundancy. Focus on structure, functions, names of variable and
#on commenting your code.
#Once you have written a clean code that returns the same thing than
#yesterday, try adding one option to your script that could be of use to the
#biologist that is looking for a pattern in the DNA sequence.

a="ATGTATCTAGATCGATCGACGATCGATCGGATCGATCGGGATCGATCGAGAGAGCTAGCTTAGAGAGAGCTAGAGCTAGCATCGATTATCGATCG"
#Return the number of non-overlapping occurrences of substring sub in string S[start:end].
A1=a.count("A")
A2=a.count("T")
A3=a.count("G")
A4=a.count("C")
p1=p2=p3=p4=0
if A1+A2+A3+A4==len(a):
    print float(A1+A3)/len(a)
    print(len(a))
    p1=a.count("CTA")
    p2=a.count("CTG")
    p3=a.count("CTC")
    p4=a.count("CTT")
if p1>0:
    print "found"
if p2>0:
    print "found"
if p3>0:
    print "found"
if p4>0:
    print "found"

#Define some functions
#Write the following functions for lists of integer:
#- coun_odd to get the number of odd numbers in the given list.
#- get_even to get the list of all even numbers in the given list.
#- arith_mean which returns the arithmetic mean of values given in the lis.
#- median that return the median of values given in the list.
#Use the above functions to display the number of odd numbers, the list of even
#numbers,
#the arithmetic mean, and the median of the numerical list entered by the user.
#Bonus 1: Can you solve the problem with numpy functions?
#Bonus 2: stop one of these functions with a warning if there are other types than
#integers in your input list.



#coun_odd to get the number of odd numbers in the given list.
def coun_odd(oddnum):
	for num in oddnum:
	   if num % 2 == 0:
	       oddnum.remove(num) 
	print oddnum
	return oddnum
coun_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

#get_even to get the list of all even numbers in the given list.	   
def coun_even(evennum):
	for num in evennum:
	   if num % 2 == 1:
	       evennum.remove(num) 
	print evennum
	return evennum
coun_even([1,2,3,4,5,6,7,8,9,10,11,12,13,14])	  


#- arith_mean which returns the arithmetic mean of values given in the lis.    
def arith_mean(numbers):
	return float(sum(numbers)) / max(len(numbers), 1)
arith_mean([1,2,3,4,5,17,30,54])	
	
#median that return the median of values given in the list.
def median(numbers):
	return np.median(numbers)
median([1,2,3,4,5,17,30,54])	



#Exercise 4 =Homework4

#* Write a program in a file called "exercise_day4.py"
#* Once the program is done, upload it in your github.

import os, sys, warnings
os.chdir('/Users/VARG/python_ebc_2016/day_04/exercise')
f=open('lulu_mix_16.csv','r')
data=f.readlines()

import sh

class Song(object):
    def __init__(self, title, artist, duration):

        self.title = title
        self.artist = artist
        try:
            self.duration = int(duration)
        except ValueError:
            warnings.warn("It's set to zero." % self.title)
            self.duration = 0

        if self.duration < 0:
            raise Exception("for negative duration " + self.title)

    def pretty_duration(self):
        secs     = self.duration
        mins     = secs / 60
        hours    = mins / 60
        return "%02i hours %02i minutes %02i seconds" % (hours, secs % 60, mins % 60)

    def play(self):
        """ webbrowser, Build the URL"""
        base_url = "https://www.youtube.com/results?search_query="
        complete_url = base_url + self.title.replace(' ','+')
        # Depends on your operating system #
        import webbrowser
        webbrowser.open(complete_url)

