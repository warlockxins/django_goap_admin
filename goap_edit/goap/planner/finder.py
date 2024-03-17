from typing import Dict, List
from .planConfig import Gaction, Gnode, Goal, PlanConfig


def searchGoal(list: List[Goal], next_state: Dict[str, bool]):
    for g in range(len(list)):
        if list[g]["state"].items() <= next_state.items():
            return list[g]
    return None


class Finder:
    def __init__(self, data: PlanConfig):
        self.config = data
        self.nodes: List[Gnode] = []
        self.cheapest = 10000

    def execute(self):
        g = Gnode("start", None, self.config["world_state"].copy(), 0)
        self.nodes.append(g)
        leaf = self.build_graph(0, self.config["actions"])

        idx_option = leaf

        leaves: List[str] = []

        while idx_option != None:
            leaves.append(self.nodes[idx_option].id)
            idx_option = self.nodes[idx_option].from_node

        if len(leaves) > 0:
            leaves.pop()
        leaves.reverse()
        return leaves

    def build_graph(self, start_node_index: int, available_actions: Dict[str, Gaction]):
        start_node = self.nodes[start_node_index]
        if start_node == None:
            return None

        leaf = None

        next_state_base = start_node.state.copy()
        running_cost = start_node.running_cost

        for key, action in available_actions.items():
            has_preconditions = action["pre_state"].items(
            ) <= next_state_base.items()

            if has_preconditions:
                cost = running_cost + action["cost"]
                if cost > self.cheapest:
                    continue

                next_state = next_state_base.copy()
                next_state = {**next_state, **action["post_state"]}

                all_goals = self.config["goals"]
                matching_goal = searchGoal(all_goals, next_state)

                next_node = Gnode(key, start_node_index,
                                  next_state.copy(), cost)
                self.nodes.append(next_node)

                if matching_goal != None:
                    if self.cheapest > cost:
                        existing_size = len(self.nodes) - 1
                        leaf = existing_size
                        self.cheapest = cost
                else:
                    next_available_actions = available_actions.copy()
                    next_available_actions.pop(key, None)

                    leaf_internal = self.build_graph(
                        len(self.nodes) - 1, next_available_actions)

                    if leaf_internal != None:
                        leaf = leaf_internal

        return leaf
