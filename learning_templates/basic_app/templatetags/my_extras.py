from django import templates

register = template.Library()

def cut(value,arg):
    """
    This cuts of all values of arg from the string
    """
    return value.replace(arg,'')

register.filter('cut', cut)    
