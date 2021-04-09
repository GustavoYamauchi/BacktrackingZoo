import numpy as np
from functools import reduce
from operator import sub

class Constraint():
    def __init__(self, variables):
        self.variables = variables
    
    def isSatisfied(self, variableToDomain):
        return True

    def removeInvalidDomains(self, _0, _1, domains):
        return domains

class NotEqual(Constraint):
    def __init__(self, v1, v2):
        super().__init__([v1, v2])
        self.variables = [v1, v2]
    
    def isSatisfied(self, variableToDomain):
        if not all(variable in variableToDomain for variable in self.variables):
            return True
        domains = [variableToDomain[variable] for variable in self.variables]
        return len(set(domains)) == len(domains)

    def removeInvalidDomains(self, chosenVariable, chosenDomain, domains):
        otherVariable = list(filter(lambda var: var != chosenVariable, self.variables))[0]

        domains[otherVariable] = np.fromiter((domain for domain in domains[otherVariable] if domain != chosenDomain), dtype=domains[otherVariable].dtype)

        return domains

    def __str__(self):
        return f"The domain of {self.variables[0]} should not be equal to {self.variables[1]}"

class Equal(Constraint):
    def __init__(self, v1, v2):
        super().__init__([v1, v2])
        self.variables = [v1, v2]

    def isSatisfied(self, variableToDomain):
        if not all(variable in variableToDomain for variable in self.variables):
            return True
        domains = [variableToDomain[variable] for variable in self.variables]
        return len(set(domains)) == 1

    def removeInvalidDomains(self, chosenVariable, chosenDomain, domains):
        otherVariable = list(filter(lambda var: var != chosenVariable, self.variables))[0]

        domains[otherVariable] = np.fromiter((domain for domain in domains[otherVariable] if domain == chosenDomain), dtype=domains[otherVariable].dtype)

        return domains

    def __str__(self):
        return f"The domain of {self.variables[0]} should be equal to {self.variables[1]}"

class NotAdjacent(Constraint):
    def __init__(self, v1, v2):
        super().__init__([v1, v2])
        self.variables = [v1, v2]

    def isSatisfied(self, variableToDomain):
        if not all(variable in variableToDomain for variable in self.variables):
            return True
        domains = [variableToDomain[variable] for variable in self.variables]
        return abs(reduce(sub, domains)) > 1

    def removeInvalidDomains(self, chosenVariable, chosenDomain, domains):
        otherVariable = list(filter(lambda var: var != chosenVariable, self.variables))[0]

        domains[otherVariable] = np.fromiter((domain for domain in domains[otherVariable] if abs(domain - chosenDomain) > 1), dtype=domains[otherVariable].dtype)

        return domains

    def __str__(self):
        return f"The domain of {self.variables[0]} should not be adjacent to {self.variables[1]}"

class SpecificDomain(Constraint):
    def __init__(self, v1, d):
        super().__init__([v1])
        self.variables = [v1]
        self.domain = d

    def isSatisfied(self, variableToDomain):
        variable = self.variables[0]
        if not variable in variableToDomain:
            return True
        choosenDomain = variableToDomain[variable]
        return self.domain == choosenDomain

    def removeInvalidDomains(self, _0, _1, domains):
        return domains

    def __str__(self):
        return f"The domain of {self.variables[0]} should be equal to {self.domain}"