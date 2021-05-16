"""
The core route-finder
"""
from typing import List, Union
from route_api.models import Routes

def find_best_path(node_from: int, node_to: int, current_path=[], best_path = []) -> Union[List[int], str]:
    """
    Given a from and to node, find the best path
    return a list of 2 or more nodes (as int)
    OR an error message
    recursive procedure, depth-first
    """

    if not current_path:
        current_path = [node_from]
    best_path_len = len(best_path)
    next_node_as_a = set([n[0] for n in Routes.objects.filter(node_a = node_from).all().values_list('node_b')])
    next_node_as_b = set([n[0] for n in Routes.objects.filter(node_b = node_from).all().values_list('node_a')])
    reachable_nodes = next_node_as_a.union(next_node_as_b) - set(current_path)
    if node_to in reachable_nodes:
        # Found a possible path
        good_path = current_path + [node_to]
        if best_path_len <= 0 or len(good_path) < len(best_path):
            best_path = good_path.copy()
        return best_path

    else:
        if best_path_len <= 0 or len(current_path) < best_path_len:  # `else already longer than current best path
            for next_a in reachable_nodes:
                depth = len(current_path)
                best_path = find_best_path(next_a, node_to, current_path + [next_a], best_path)

        return best_path
