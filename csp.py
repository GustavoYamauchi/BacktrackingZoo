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
                np.append(self.constraints[variable], constraint)

    def isValid(self, variable, variableToDomain):
        for constraint in self.constraints[variable]:
            if not constraint.isSatisfied(variableToDomain):
                return False
        return True
    
    def backtrackingSearch(self, variableToDomain = {}):
        print(f"{len(variableToDomain)} - {len(self.variables)} \n {variableToDomain}")
        if len(variableToDomain) == len(self.variables):
            print("Parou")
            return variableToDomain

        remainingVariables = np.setdiff1d(self.variables, list(variableToDomain.keys()), True)
        # copyDomain = 
    
        chosenVariable = remainingVariables[0]
        for value in self.domains[chosenVariable]:
            variableToDomainLocal = variableToDomain.copy()
            variableToDomainLocal[chosenVariable] = value

            if self.isValid(chosenVariable, variableToDomainLocal):
                # forwardChecking(remainingVariables, variableToDomainLocal, )
                result = self.backtrackingSearch(variableToDomainLocal)
                if result is not None:
                    return result
        return None

    def forwardChecking(self, remainingVariables, variableToDomain, domain):
        for variable in remainingVariables:
            for constraint in self.constraints[variable]:
                if not constraint.isSatisfied(variableToDomain):
                    domains[variable] = domains[variable != domain]
                    # a = np.array([1,2,3,4])
                    # print(a[a != 3]) 