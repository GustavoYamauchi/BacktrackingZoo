import numpy as np

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




        # # Não analise se todos os estados estiverem atribu;idos
        # if not all(variavel in atribuicao for variavel in self.variaveis):
        #   return True
        # # cores de estados vizinhos não podem ser igual
        # valores = [atribuicao[variavel] for variavel in self.variaveis]
        # return len(set(valores)) == len(valores)