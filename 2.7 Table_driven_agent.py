
def table_driven_agent(percept):
    percepts=[]
    table=[['taco','masticar'],['comer','move']]
    percepts.append(percept)
    action = lookup(percept,table)
    if action == 'move':
       action = move(percept[1])
    return(action)
def lookup(percept,table):
    for i in table:
        if i[0] == percept[0]:
            return(i[1])
def move(percept):
    if percept == 'izquierda':
        return('ahogarse con el taco')
    elif percept == 'Derecha':
        return('masticar taco')
percept = list(map(str,input("Ingresa el estado y la posicion: ").split(',')))
action = table_driven_agent(percept)
print(action)
        
            
    
    
