from django import template

register = template.Library()

@register.filter(name='range') 
def add_range(number):
    return range(1,number)

# @register.filter(name='inter')
# def add_inter(inter):
#     return 