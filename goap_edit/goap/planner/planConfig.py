from typing import Dict, List, TypedDict


class Gnode:
    def __init__(self, id: str, from_node: int, state: Dict[str, bool], running_cost: int):
        self.id = id
        self.from_node = from_node
        self.state = state
        self.running_cost = running_cost


class Gaction(TypedDict):
    cost: int
    pre_state: Dict[str, bool]
    post_state: Dict[str, bool]


class Goal(TypedDict):
    name: str
    state: Dict[str, bool]


class PlanConfig(TypedDict):
    actions: Dict[str, Gaction]
    world_state: Dict[str, bool]
    goals: List[Goal]
