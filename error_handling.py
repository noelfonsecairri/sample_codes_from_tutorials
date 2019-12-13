import sys

def linux_interaction(x):
	assert (x in sys.platform), "this error will appear when string is not in sys.platform"
	print('linux function successfully executed')

try:
	linux_interaction('x') 
except AssertionError as error: 
	print(error)
else:
	try:
		with open('file.log') as file:
			read_data = file.read()
	except FileNotFoundError as fnf_error:
		print(fnf_error)
finally:
	print('Cleaning up, irrespective on any exceptions')