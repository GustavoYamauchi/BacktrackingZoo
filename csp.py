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

    def mcv(self, remainingVariables):
        maxCount = float('-inf')
        chosenVariable = ""
        for variable in remainingVariables:
            if len(self.constraints[variable]) > maxCount:
                maxCount = len(self.constraints[variable])
                chosenVariable = variable
        return chosenVariable

    def mrv(self, remainingVariables):
        minOccurence = float('inf')
        chosenVariable = ""
        for variable in remainingVariables:
            if len(self.domains[variable]) < minOccurence:
                minOccurence = len(self.domains[variable])
                chosenVariable = variable
        return chosenVariable

    def backtrackingSearch(self, useMRV, variableToDomain = {}):
        if len(variableToDomain) == len(self.variables):
            return variableToDomain

        remainingVariables = np.setdiff1d(self.variables, list(variableToDomain.keys()), True)
        
        chosenVariable = self.mrv(remainingVariables) if useMRV else self.mcv(remainingVariables)

        for domain in self.domains[chosenVariable]:
            variableToDomainLocal = variableToDomain.copy()
            variableToDomainLocal[chosenVariable] = domain
            domainsCopy = self.domains.copy()

            if self.isValid(chosenVariable, variableToDomainLocal):
                self.forwardChecking(chosenVariable, domain)
                print(f"Set variables: {variableToDomainLocal}")
                result = self.backtrackingSearch(useMRV, variableToDomainLocal)

                if result is not None:                    
                    return result

            self.domains = domainsCopy
        print(f"Backtracking: {variableToDomain}")
        return None

    def forwardChecking(self, chosenVariable, chosenDomain):
        for constraint in self.constraints[chosenVariable]:
            self.domains = constraint.removeInvalidDomains(chosenVariable, chosenDomain, self.domains)