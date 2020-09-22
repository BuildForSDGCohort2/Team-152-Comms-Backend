
from django import template

register = template.Library()

@register.filter
def expand(value):
    """
    Expand a given list of courses.

    input: ['Graphic Design', 'Backend Development']
    result: Graphic Design, Backend Development
    """

    return ', '.join(value)
