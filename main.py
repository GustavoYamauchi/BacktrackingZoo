import numpy as np
from csp import CSP
from constraint import *

def getOptimization():
	print("Select optimization: 0 - MCV | 1 - MRV")
	inputString = -1	
	
	while inputString not in ["0", "1"]:
	    inputString = input()
	    if inputString == "0": 
	        result = False
	    elif inputString == "1":
	        result = True
	    else:
	       	print("Invalid input, try again (0 - MCV | 1 - MRV)")
	print()
	return result

variables = np.array(["Leão","Antílope","Hiena","Tigre","Pavão","Suricato","Javali"])
domains = {}
for variable in variables:
    domains[variable] = np.array([1, 2, 3, 4])
problem = CSP(variables, domains)
problem.addConstraint(NotEqual("Leão", "Tigre"))
problem.addConstraint(NotEqual("Leão", "Pavão"))
problem.addConstraint(NotEqual("Tigre", "Suricato"))
problem.addConstraint(NotEqual("Tigre", "Javali"))
problem.addConstraint(NotEqual("Tigre", "Pavão"))
problem.addConstraint(Equal("Suricato", "Javali"))
problem.addConstraint(NotEqual("Hiena", "Leão"))
problem.addConstraint(NotEqual("Hiena", "Antílope"))
problem.addConstraint(NotEqual("Hiena", "Pavão"))
problem.addConstraint(NotEqual("Hiena", "Suricato"))
problem.addConstraint(NotEqual("Hiena", "Javali"))
problem.addConstraint(NotAdjacent("Antílope", "Leão"))
problem.addConstraint(NotAdjacent("Antílope", "Tigre"))
problem.addConstraint(SpecificDomain("Leão", 1))
result = problem.backtrackingSearch(getOptimization())
print()
print("Answer not found" if result is None else f"Answer: {result}")