from django.contrib import admin

# Register your models here.

# ActionStateMembership, ActionState
from .models import PlanDomain, Variable, Goal, Action, ActionState, GoalState

from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


class VariableTabularInline(admin.TabularInline):
    extra = 1
    model = Variable
    classes = ['collapse']


class GoalStateTabularInline(admin.TabularInline):
    extra = 1
    model = GoalState

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "variable":
            parent_id = request.resolver_match.kwargs['object_id']
            action = Goal.objects.all().filter(id=parent_id).first()
            planDomainId = action.planDomain.id
            kwargs["queryset"] = Variable.objects.filter(
                plan_domain_id=planDomainId)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class GoalTabularInline(admin.TabularInline):
    extra = 1
    model = Goal
    show_change_link = True
    classes = ("collapse",)


class GoalAdmin(admin.ModelAdmin):
    model = Goal
    show_change_link = True

    inlines = [GoalStateTabularInline]


class ActionStateTabularInline(admin.options.TabularInline):
    model = ActionState
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "variable":
            parent_id = request.resolver_match.kwargs['object_id']
            action = Action.objects.all().filter(id=parent_id).first()
            planDomainId = action.planDomain.id
            kwargs["queryset"] = Variable.objects.filter(
                plan_domain_id=planDomainId)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ActionAdmin(admin.ModelAdmin):
    extra = 1
    inlines = [ActionStateTabularInline]
    view_on_site = False
    readonly_fields = ("planDomain",)

    list_display = ('name', )

    class Meta:
        model = Action


class ActionTabularInline(admin.options.TabularInline):
    extra = 1
    # inlines = [ActionStateTabularInline]
    model = Action
    show_change_link = True


class PlanDomainAdmin(admin.ModelAdmin):
    inlines = [VariableTabularInline, GoalTabularInline,
               ActionTabularInline
               ]
    extra = 1
    allow_tags = True

    class Meta:
        model = PlanDomain


admin.site.register(PlanDomain, PlanDomainAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Goal, GoalAdmin)
