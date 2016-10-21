#import os, sys, warnings
#os.chdir('/Users/VARG/python_ebc_2016/day_05/exercise')
#
#

class FastaParser(object):
	"""docstring for ClassName"""
	def __init__(self, path):
		self.path = path 
		f = open(self.path,'r')
		self.raw_data = f.readlines()
		f.close()
		seq_dict = {}
		for l in raw_data:
			my_line = l[:-1]
			if my_line[0] == '>':
				my_id = my_line[1:]
				seq_dict[my_id] = ''
			else: 
				seq_dict[my_id] = seq_dict[my_id] + my_line

		self.seq_dict = seq_dict 
		self.count = len(seq_dict)
		self.true_length=[len(s) for s in seq_dict.values()]
		print seq_dict
		if seq_dict >self.true_length
		print " the sequence number is too high " 

		if not os.path.exists(self.path):
			raise IOError('the file is not there') 
			
			
	def description(self):
 			

#to find the path in ipython first you nee to import os and then use os.chdir

#import os 
#os.chdir("/Users/VARG/python_ebc_2016/day_05/exercise")

#run the exercise_day5 with de funtion execfile like this: execfile('exercise_day5.py')

