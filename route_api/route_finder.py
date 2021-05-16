"""
The core route-finder
"""
from typing import List, Union
from route_api.models import Routes

def find_best_path(node_from: int, node_to: int, current_path=[]) -> Union[List[int], str]:
    """
    Given a from and to node, find the best path
    return a list of 2 or more nodes (as int)
    OR an error message
    """

    start_node_as_a = set([n[0] for n in Routes.objects.filter(node_a = node_from).all().values_list('node_b')])
    start_node_as_b = set([n[0] for n in Routes.objects.filter(node_b = node_from).all().values_list('node_a')])
    reachable_nodes = start_node_as_a.union(start_node_as_b) - set(current_path)
    if node_to in reachable_nodes:
        print ("Found it!")
        return [node_from]
    else:

        for next_a in reachable_nodes:
            this_path = current_path
            this_path.append(node_from)
            more = find_best_path(next_a, node_to, this_path)
            this_path.append(more)

    print ("YO")