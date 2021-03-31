# print("Deseja utilizar: 0 - MCV | 1 - MRV")
# inputString = -1

# # mcv() if inputString == 0 else mrv()


# while inputString not in ["0", "1"]:
#     inputString = input()
#     if inputString == "0": 
#         resultado = "mcv"
#     elif inputString == "1":
#         resultado = "mrv" 
#     else:
#         resultado = "Entrada invalida, tente novamente (0 - MCV | 1 - MRV)"

#     print(resultado)



# MRV -> Escolher a variável com menos opções de valores
# MCV -> Escolher a variável com mais restrições


import numpy as np
from csp import Constraints
from constraint import *

variables = np.array(["Leão","Antílope","Hiena","Tigre","Pavão","Suricato","Javali"])
domains = {}
for variable in variables:
    domains[variable] = np.array([1, 2, 3, 4])
problem = Constraints(variables, domains)
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
result = problem.backtrackingSearch()
print("Answer not found" if result is None else result)