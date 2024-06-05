
"""
Created by: Tanner Hammond
Date: June 2024
Python ver. 3.9.16

Parameters:
script: Path to other script you will be testing. Can be a full or partial path.
Iterations: Number of times to run the script for each condition defined in `params`.
params: Dictionary with values for different field values to test. Keys should be object names, with a list of values to iterate through. Multiple objects can be used.
variables: Variables from the other script to track in the output dictionary.

"""

def scriptTimer(script,iterations=1,params={},variables=[]):
	import time
	#Setup output dictionary
	outDict = {}
	outDict.setdefault('Runtime', [])
	outDict.setdefault('Error', [])
	if params != {}:
		for var in params:
			outDict.setdefault(var,[])
	if variables != []:
		for var in variables:
			outDict.setdefault(var,[])

	#Set Variables
	for iteration in range(len(params[next(iter(params))])):
		for each in range(iterations):
			if params != {}:
				for field in params:
					locals()[field] = params[field][iteration]
			#GET LIST OF VARS

			#Import and Run Script
			localvariables = {}
			with open(script) as file:
				startTime = time.time()
				try:
					exec(file.read(),locals(),localvariables)
				except Exception as e:
					endTime = time.time()
					outDict['Runtime'].append(endTime - startTime)
					outDict['Error'].append(type(e).__name__)
					if params != {}:
						for var in params:
								try:
									outDict[var].append(locals()[var])
								except:
									outDict[var].append('<no value>')
					if variables != []:
						for var in variables:
							try:
								outDict[var].append(localvariables[var])
							except:
								outDict[var].append('<no value>')
					break

			endTime = time.time()

			outDict['Runtime'].append(endTime - startTime)
			outDict['Error'].append(None)
			if params != {}:
				for var in params:
						outDict[var].append(locals()[var])
			if variables != []:
				for var in variables:
						outDict[var].append(localvariables[var])

				#CLEAR USING PREVIOUS VARS LIST
	return outDict

"""
#Usage Example:
OtherScript.py
```
c = a + b
d = c + 1
```

main.py
```
#import scriptTimer #or paste into code

script = 'OtherScript.py'
iterations = 3
params = {'a':[1,2,3,'',1],
		'b':[6,5,4,3,'']}
variables = ['d']

outDict = scriptTimer(script,iterations,params,variables)

print(outDict)
```

Output:
{'Runtime': [0.023, 0.019, 0.012, 0.013, 0.009, 0.007, 0.017, 0.011, 0.019, 0.016, 0.015], 
 'Error': [None, None, None, None, None, None, None, None, None, 'TypeError', 'TypeError'], 
 'a': [1, 1, 1, 2, 2, 2, 3, 3, 3, '', 1], 
 'b': [6, 6, 6, 5, 5, 5, 4, 4, 4, 3, ''], 
 'd': [8, 8, 8, 8, 8, 8, 8, 8, 8, '<no value>', '<no value>']}
"""