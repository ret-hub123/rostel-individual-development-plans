"""from django import template
from django.template.defaultfilters import date, timeuntil
from datetime import datetime

register = template.Library()

@register.filter
def days_left(value):

    #value = value.strftime("%b. %d, %Y")

    if value:
        delta = ((datetime.strptime(date(value), "%B %d, %Y").date() -
                datetime.now().date()))


        if delta.days < 0:
            return "death"
        elif delta.days <= 3:
            return "warning"
        else:
            return "good"
    else:
        return 0



"""

from django import template
from datetime import datetime, date

register = template.Library()


@register.filter
def days_left(value):

    if isinstance(value, datetime):
        value = value.date()

    today = date.today()
    delta = (value - today).days

    if delta < 0:
        return "death"
    elif delta <= 3:
        return "warning"
    return "good"