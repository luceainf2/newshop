from django import template
register = template.Library()


@register.filter
def short_description(description, max_length=100):
    if len(description) > max_length:
        return description[:max_length] + "..."
    return description
