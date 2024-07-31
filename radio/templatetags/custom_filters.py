# radio/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    if 'youtu.be' in value:
        video_id = value.split('/')[-1].split('?')[0]
        return f'https://www.youtube.com/embed/{video_id}'
    elif 'youtube.com/watch' in value:
        video_id = value.split('v=')[-1].split('&')[0]
        return f'https://www.youtube.com/embed/{video_id}'
    return value

@register.filter(name='facebook_embed_url')
def facebook_embed_url(value):
    if 'facebook.com' in value:
        return f'https://www.facebook.com/plugins/video.php?href={value}&show_text=0&width=560'
    return value


@register.filter
def startswith(value, arg):
    return value.startswith(arg)