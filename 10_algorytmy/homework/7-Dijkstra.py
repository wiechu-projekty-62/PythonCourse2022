graph = {
    'A': {'B' : 2, 'D' : 4},
    'B': {'C' : 3, 'D' : 3},
    'C': {'E' : 2},
    'D': {'C' : 3, 'E': 4},
    'E': {}
}

def get_cheapest_node(costs_dict, processed_list):
    cheapest_cost = float('inf')
    cheapest_key = None

    for name, cost in costs_dict.items():
        if name not in processed_list and cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_key = name
    return cheapest_key

costs = {}
parents = {}

for name in graph.keys():
    costs[name] = float('inf')

processed = []
current_node = 'A'
costs[current_node] = 0
parents[current_node] = None

while current_node:

    #calculate cost of the neighbours
    for neighbour in graph[current_node]:
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node

    processed.append(current_node)
    current_node = get_cheapest_node(costs, processed)


for d, c in costs.items():
    print(f'The cost for {d} is {c}')

    current_d = d
    while parents[current_d]:
        print(current_d)
        current_d = parents[current_d]
    else:
        print(current_d)
