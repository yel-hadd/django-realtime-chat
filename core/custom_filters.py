from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        css_classes += f' {arg}'
    else:
        css_classes = arg
    value.field.widget.attrs['class'] = css_classes
    return value
