def constraint_func(names, values):
    return values[0] != values[1]
def is_consistant(variable,value,ass,const):
    for (var1,var2) in const:
        if var1==variable and var2 in ass:
            if not constraint_func((var1,var2),(value,ass[var2])):
                                   return False
        if var2==variable and var1 in ass:
            if not constraint_func((var1,var2),(ass[var1],value)):
                                   return False
    return True
def backtrack(variables,domain,const,ass):
    if len(ass)==len(variables):
        return ass
    unass=[v for v in variables if v not in ass]
    variable=unass[0]
    for value in domain:
        if is_consistant(variable,value,ass,const):
            ass[variable]=value
            result=backtrack(variables,domain,const,ass)
            if result:
                return result
            ass.pop(variable)
    return None
names=['A','B','C','D',]
color=["red","green","blue"]
const=[('A','B'),('A','C'),('B','C'),('B','D'),('C','D')]
ass={}
output=backtrack(names,color,const,ass)
print("\n color mapping:\n")
for k,v in output.items():
    print(k,"=>",v)
    
        

            
