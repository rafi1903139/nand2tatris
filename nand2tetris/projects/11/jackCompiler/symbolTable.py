from constant import * 

class SymbolTable :
    def __init__(self):

        self.cnt_static = 0
        self.cnt_field = 0
        self.cnt_arg = 0
        self.cnt_var = 0

        self.table = []

    def reset(self):

        self.table.clear()
        self.cnt_arg =  0 
        self.cnt_field = 0
        self.cnt_static = 0
        self.cnt_var = 0

    def define(self, name, varType, kind):

        entry = {'name': name, 'type': varType, 'kind': kind,}

        if kind == VAR_STATIC:
            entry['index'] = self.cnt_static 
            self.cnt_static += 1 
        elif kind == VAR_FIELD:
            entry['index'] = self.cnt_field
            self.cnt_field += 1
        elif kind == VAR_ARG:
            entry['index'] = self.cnt_arg 
            self.cnt_arg += 1 
        elif kind == VAR_VAR:
            entry['index'] = self.cnt_var 
            self.cnt_var += 1 
        else:
            return 

        self.table.append(entry)

    def varCount(self, kind):
        if kind == VAR_STATIC:
            return self.cnt_static 
        elif kind == VAR_FIELD:
            return self.cnt_field 
        elif kind == VAR_VAR:
            return self.cnt_var 
        elif kind == VAR_ARG:
            return self.cnt_arg 
        else:
            return None
    
    def kindOf(self, name):
        for entry in self.table:
            if entry['name'] == name:
                return entry['kind'] 
        
        return None

    def typeOf(self, name):
        for entry in self.table:
            if entry['name'] == name:
                return entry['type'] 
        
        return None

    def indexOf(self, name):
        for entry in self.table:
            if entry['name'] == name:
                return entry['index'] 
        
        return None

