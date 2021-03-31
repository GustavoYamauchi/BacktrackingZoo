import numpy as np
from functools import reduce

class Constraint():
    def __init__(self, variables):
        self.variables = variables
    
    def isSatisfied(self, variableToDomain):
        return True

class NotEqual(Constraint):
    def __init__(self, v1, v2):
        super().__init__([v1, v2])
        self.variables = [v1, v2]
    
    def isSatisfied(self, variableToDomain):
        if not all(variable in variableToDomain for variable in self.variables):
            return True
        domains = [variableToDomain[variable] for variable in self.variables]
        return len(set(domains)) == len(domains)

class Equal(Constraint):
    def __init__(self, v1, v2):
        super().__init__([v1, v2])
        self.variables = [v1, v2]

    def isSatisfied(self, variableToDomain):
        if not all(variable in variableToDomain for variable in self.variables):
            return True
        domains = [variableToDomain[variable] for variable in self.variables]
        return len(set(domains)) == 1

class NotAdjacent(Constraint):
    def __init__(self, v1, v2):
        super().__init__([v1, v2])
        self.variables = [v1, v2]

    def isSatisfied(self, variableToDomain):
        if not all(variable in variableToDomain for variable in self.variables):
            return True
        domains = [variableToDomain[variable] for variable in self.variables]
        return abs(reduce(lambda total, element: total - variableToDomain[element])) > 1