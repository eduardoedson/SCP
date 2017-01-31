from django import template

register = template.Library()


@register.filter('has_group')
def has_group(user, grupo):
    groups = user.groups.all().values_list('name', flat=True)
    return True if grupo in groups else False
