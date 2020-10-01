from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(start):
  return range(start)
