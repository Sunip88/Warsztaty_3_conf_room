#!/usr/bin/python3.7
from django import template

register = template.Library()


@register.filter(name='change_bool')
def trueorfalse(var_bool):
    if var_bool:
        return 'Tak'
    else:
        return 'Nie'

