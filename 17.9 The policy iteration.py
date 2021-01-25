nos = 4  # numero de estyados
A = ['l', 'r']  # acciones
noa = 2

# R [desde estado][acion]
R = [[-1, -1], [-1, -1], [-1, -1]]

# P [desde estado] [a estado] [accion]
P = [
    [[0.8, 0.2], [0.2, 0.8], [0, 0], [0, 0]],
    [[0.8, 0.2], [0, 0], [0.2, 0.8], [0, 0]],
    [[0, 0], [0.8, 0.2], [0, 0], [0.2, 0.8]],
]

delta = 0.01
gamma = 0.25
max_diff = 0

V = [0, 0, 0, 10]  # servicios públicos de cada estado


print('Iteracion', '0', '1', '2', '3', 'diferencia maxima', sep="|")

for time in range(0, 30):
    print(time, V[0], V[1], V[2], V[3], max_diff, sep="|")
    Vnew = [-1e9, -1e9, -1e9,10]
    for i in range(3):
        for a in range(noa):
            cur_val = 0
            for j in range(nos):
                cur_val += P[i][j][a]*V[j]
            cur_val *= gamma
            cur_val += R[i][a]
            Vnew[i] = max(Vnew[i], cur_val)
    max_diff = 0
    for i in range(4):
        max_diff = max(max_diff, abs(V[i]-Vnew[i]))
    V = Vnew
    if(max_diff < delta):
        break

# una última iteración para determinar la política
Vnew = [-1e9, -1e9, -1e9, 10]
policy = ['NA', 'NA', 'NA', 'NA']
for i in range(3):
    for a in range(noa):
        cur_val = 0
        for j in range(nos):
            cur_val += P[i][j][a]*V[j]
        cur_val *= gamma
        cur_val += R[i][a]
        if(Vnew[i] < cur_val):
            policy[i] = A[a]
            Vnew[i] = max(Vnew[i], cur_val)
print("La politica es:", policy)