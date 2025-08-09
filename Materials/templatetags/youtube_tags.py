import re
from django import template

register = template.Library()

@register.filter
def youtube_id(url):
    if not url:
        return ''
    regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return ''
