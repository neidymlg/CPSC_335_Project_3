# Cases:   
# times = [[1,2,1]]
# n = 2
# start_node = 1

# times = [[1,2,1]]
# n = 2
# start_node = 2

#returns minimum time it takes for all nodes to get network update using Floyd Warshall algorithm
def get_total_time(times, n, start_node):
    #array to hold matrix A0, A1, to An
    combo_arr = []  

    #create a n*n matrix, where [0,0], [1,1] and so on are all 0 
    #to anticipate for values that are not connected to themselves
    #everything else is initalized as infinity as default
    #to anticipat for noed that are not going to be reached
    for i in range(0,n):
        combo_arr.append([float('inf')] * n)
        combo_arr[i][i] = 0

    #initalizes all node connects
    #[starting node] * [ending node] = edge
    for i in range(0, len(times)):
        combo_arr[times[i][0]-1][times[i][1]-1] = times[i][2]

    #Floyd Warshall algorithm, in which it takes the minimum of the past cell
    #or the minimum of two other cells EX: A2[3,1] = min(A1[3,1], A1[3,2]+A1[2,1])
    for i in range(0, n):
        for j in range(0,n):
            for k in range(0,n):
                combo_arr[j][k] = min(combo_arr[j][k], combo_arr[j][i] + combo_arr[i][k])
    
    #for finding the maximum value
    #will skip itself as we are already at that node and do not have to connect to itself again
    #Ex: 1 -> 1 has an edge of 55, even though 55 is the max, the starting node is 1, so we 
    # ignore it since we are at 1
    best = 0
    for i in range(0, n):
        if(combo_arr[start_node-1][i] > best and start_node != i+1):
            best = combo_arr[start_node-1][i]

    #if any of the results were infinity, that means that the starting node couldn't reach it
    #if all results are 0, this is probably a input error in times array as time must flow
    #else return the minimum amount of time it took for all nodes to receive the message
    if best == 0 or best == float('inf'):
        return -1
    else:
        return best

#times of node, [starting node] [destination] [edge]
#number of nodes = n
#where the message starts at and must be passed from
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
start_node = 2

print(f'Minimum time for all nodes to get the message: {get_total_time(times, n, start_node)}')
