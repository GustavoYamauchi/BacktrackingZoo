import numpy as np

class Constraints:
    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = np.array([])
            if variable not in self.domains:
                raise LookupError("Each variable needs a domain.")


    def addConstraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable is not defined before")
            else:
                self.constraints[variable] = np.append(self.constraints[variable], constraint)
                # print(self.constraints)

    def isValid(self, variable, variableToDomain):
        for constraint in self.constraints[variable]:
            if not constraint.isSatisfied(variableToDomain):
                return False
        return True
    
    def backtrackingSearch(self, variableToDomain = {}):
        if len(variableToDomain) == len(self.variables):
            return variableToDomain

        remainingVariables = np.setdiff1d(self.variables, list(variableToDomain.keys()), True)
    
        chosenVariable = remainingVariables[0]
        for domain in self.domains[chosenVariable]:
            variableToDomainLocal = variableToDomain.copy()
            variableToDomainLocal[chosenVariable] = domain

            if self.isValid(chosenVariable, variableToDomainLocal):
                self.forwardChecking(chosenVariable)
                result = self.backtrackingSearch(variableToDomainLocal)
                if result is not None:
                    return result
        return None

    def forwardChecking(self, chosenVariable):
        for constraint in self.constraints[chosenVariable]:
            print(constraint)
            # TODO: Remover dominios das variaveis em que a chosenVariable possui uma restrição