import queue
import copy

global step
step = 0
q = queue.LifoQueue()
d = {}

data = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]

start = data

goal = [
    [8,1,3],
    [2,4,5],
    [7,6,0]
]

q.put(data)

def find_zero(data):
    for a in range(len(data)):
        for b in range(len(data)):
            if data[a][b] == 0:
                return (a,b)
            
def mapping(parent, child):
    parent_tuple = (tuple(parent[0]), tuple(parent[1]), tuple(parent[2]))
    child_tuple = (tuple(child[0]), tuple(child[1]), tuple(child[2]))
    d[child_tuple] = parent_tuple
            
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
                q.put(swapped)
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

explored = []

while q.not_empty:
    data = q.get()
    explored.append(data)
    result = slide(data)
    if result != False:
        break

tuple_goal = (tuple(goal[0]), tuple(goal[1]), tuple(goal[2]))
print_step(tuple_goal)

print("Jumlah step yang dicoba = ", len(explored))
print("Jumlah langkah = ", step)