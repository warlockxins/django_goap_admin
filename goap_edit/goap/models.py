from django.db import models


class PlanDomain(models.Model):
    description = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.description

    def get_absolute_url(self):

        return "people-detail/" + str(self.id)


class Variable(models.Model):
    plan_domain = models.ForeignKey(PlanDomain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Goal(models.Model):
    planDomain = models.ForeignKey(PlanDomain, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, default='unspecified')

    def __str__(self):
        return self.name


class GoalState(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    variable = models.OneToOneField(Variable, on_delete=models.CASCADE)
    value = models.BooleanField(default=False)

    def __str__(self):
        return self.variable.name


class Action(models.Model):
    planDomain = models.ForeignKey(PlanDomain, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    cost = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class ActionState(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    value = models.BooleanField(default=False)

    PRECONDITIONS = 1
    POSTCONDITION = 2

    CONDITION_OPTIONNS = [
        (PRECONDITIONS, ("Precondition")),
        (POSTCONDITION, ("Postcondition"))
    ]

    option = models.PositiveSmallIntegerField(
        choices=CONDITION_OPTIONNS,
        default=PRECONDITIONS
    )

    def __str__(self):
        return self.variable.name
