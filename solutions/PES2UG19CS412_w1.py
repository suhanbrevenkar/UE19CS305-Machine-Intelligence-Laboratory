import heapq

def A_star_Traversal(cost, heuristic, start_point, goals):
    
    path = []
    #TODO
    if start_point in goals:
    	return [start_point]
    
    graph_vertex = [(0, 0, start_point, [start_point])]
    heapq.heapify(graph_vertex)
    nodes_index = {}
    nodes_index[start_point] = 0
    
    while True:
    	fn, sum_of_path, vertex, path = heapq.heappop(graph_vertex)
    	nodes_index[vertex] = -1

    	if vertex in goals:
    		return path    		

    	for s in range(1, len(cost)):
    		if cost[vertex][s] != -1 and vertex != s:
    			if s in nodes_index and nodes_index[s] != -1:
    				if graph_vertex[nodes_index[s]][0] > sum_of_path + cost[vertex][s] + heuristic[s]:
    					graph_vertex[nodes_index[s]] = (sum_of_path + cost[vertex][s] + heuristic[s], sum_of_path + cost[vertex][s], s, path+[s])
    			else:
    				heapq.heappush(graph_vertex, (sum_of_path+cost[vertex][s]+heuristic[s], sum_of_path+cost[vertex][s], s, path+[s]))
    	
    	heapq.heapify(graph_vertex)
    	for w in range(len(graph_vertex)):
    		nodes_index[graph_vertex[w][2]] = w
    return path


def DFS_Traversal(cost, start_point, goals):
    path = []
    explored_nodes = []
    variable_count = 0
    while(True):
        variable_count = variable_count + 1
        if(variable_count > 3*len(cost)):
            break
        if start_point in goals:
            path.append(start_point) 
            break
        if start_point not in explored_nodes :
            path.append(start_point)
            explored_nodes.append(start_point)
        for e in range(1 , (len(cost[start_point])+1)) :
            if (e == (len(cost[start_point]))):
                path.pop()
                start_point = path[-1]
                break
            if (cost[start_point][e] not in [0,-1]):
                if (e not in explored_nodes ):
                    start_point = e 
                    break
                else: continue                   
    return path


