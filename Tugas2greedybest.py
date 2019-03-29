import copy

global step
step = 0
q = []
d = {}

data = [
    [1,3,8],
    [7,2,0],
    [6,5,4]
]

start = data

global tuple_s
tuple_s = (tuple(start[0]), tuple(start[1]), tuple(start[2]))

goal = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]

q.append(data)

def find_zero(data):
    for a in range(len(data)):
        for b in range(len(data)):
            if data[a][b] == 0:
                return (a,b)
            
def slide(data):
    zero = find_zero(data)
    swap_able = [
        (zero[0]-1, zero[1]),
        (zero[0], zero[1]+1),
        (zero[0]+1, zero[1]),
        (zero[0], zero[1]-1)
    ]
    for coord in swap_able:
        if coord[0] >= 0 and coord[1] >= 0 and coord[0] <= len(data)-1 and coord[1] <= len(data[0])-1:
            temp = copy.deepcopy(data)
            swapped = swap(temp, zero, coord)
            # print_map(swapped)
            if swapped == goal:
                mapping(copy.deepcopy(data), swapped)
                return swapped
            if not check_if_explored(swapped):
                q.append(swapped)
                mapping(copy.deepcopy(data), swapped)
    return False

def swap(data, coordA, coordB):
    temp = data[coordA[0]][coordA[1]]
    data[coordA[0]][coordA[1]] = data[coordB[0]][coordB[1]]
    data[coordB[0]][coordB[1]] = temp
    return data

def check_if_explored(data):
    if data in explored:
        return True
    return False

def mapping(parent, child):
    parent_tuple = (tuple(parent[0]), tuple(parent[1]), tuple(parent[2]))
    child_tuple = (tuple(child[0]), tuple(child[1]), tuple(child[2]))
    d[child_tuple] = parent_tuple

def count_step():
    global step
    step+=1

def print_step(agoal):
    if(start==agoal):
        print('\n'.join(map(str, agoal)))
        count_step();
        return 
        
    for key, value in d.items():
        if(key == agoal):
            count_step();
            print_step(value)
            print('\n'.join(map(str, agoal)))
            print('\n')
    return

def find_h(adata,agoal):
    h = 0
    for a in range(len(adata)):
        for b in range(len(adata)):
            for c in range(len(agoal)):
                for d in range(len(agoal)):
                    if adata[a][b] != 0:
                        if adata[a][b] == agoal[c][d]:
                            h += abs(a-c)+abs(b-d)
    return h

def find_g(adata, numb):
    global tuple_s
    if (tuple_s == adata):
        return numb
    for key, value in d.items():
        if(key == adata):
            return find_g(value, numb+1)

def find_manhattan_value(adata):
    h = find_h(adata, goal)
    tuple_g = (tuple(adata[0]), tuple(adata[1]), tuple(adata[2]))
    g = find_g(tuple_g, 0)
    value = g + h
    return value
        
def find_manhattan(q):
    for index in range(len(q)):
        if (index==0):
            manhattan_list = q[0]
            manhattan_value = find_manhattan_value(q[0])
        else:
            temp = find_manhattan_value(q[index])
            if(temp < manhattan_value):
                manhattan_list = q[index]
                manhattan_value = temp
                return q.pop(index)
    return q.pop(0)

def find_best_h(q):
    for index in range(len(q)):
        if (index==0):
            manhattan_list = q[0]
            manhattan_value = find_h(q[0], goal)
        else:
            temp = find_h(q[index], goal)
            if(temp < manhattan_value):
                manhattan_list = q[index]
                manhattan_value = temp
                return q.pop(index)
    return q.pop(0)

explored = []

while q:
    data = find_best_h(q)
    explored.append(data)
    result = slide(data)
    if result != False:
        break

tuple_goal = (tuple(goal[0]), tuple(goal[1]), tuple(goal[2]))
print_step(tuple_goal)

print("Jumlah step yang dicoba = ", len(q))
print("Jumlah langkah = ", step)