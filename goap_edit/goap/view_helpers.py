from .models import PlanDomain, GoalState, ActionState


def map_states_lambda(state):
    return {
        "parameter": state.variable.name,
        "value": state.value
    }


def get_goal_state(id):
    states = GoalState.objects.all().filter(goal=id)
    d = {}
    for s in states:
        d[s.variable.name] = s.value

    return d


def make_goals_list(goals):
    return list(
        map(lambda g: {
            'name': g.name,
            'state': get_goal_state(g.id)
        }, goals
        )
    )


def get_action_state(id, dir):
    states = ActionState.objects.all().filter(action_id=id, option=dir)
    d = {}
    for s in states:
        d[s.variable.name] = s.value

    return d


def make_action_list(actions):
    d = {}

    for a in actions:
        d[a.name] = {
            'cost': a.cost,
            'pre_state': get_action_state(a.id, ActionState.PRECONDITIONS),
            'post_state': get_action_state(a.id, ActionState.POSTCONDITION),
        }

    return d


def variables_to_world_state(variables):
    d = {}

    for v in variables:
        d[v['name']] = False

    return d


def get_plan_config(id=0):
    plan = PlanDomain.objects.get(pk=id)
    variables = plan.variable_set.values('name')

    goalList = make_goals_list(plan.goal_set.all())
    actionList = make_action_list(plan.action_set.all())

    return {
        'description': plan.description,
        'world_state': variables_to_world_state(variables),
        'goals': goalList,
        'actions': actionList
    }


# def get_plan_variables(id=0):
#     plan = PlanDomain.objects.get(pk=id)
#     variables = plan.variable_set.values('name')
#
#     return variables_to_world_state(variables)
