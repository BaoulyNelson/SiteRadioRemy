from django import template
import re

register = template.Library()

@register.filter(name='youtube_embed_url')
def youtube_embed_url(value):
    if 'youtu.be' in value:
        video_id = value.split('/')[-1].split('?')[0]
        return f'https://www.youtube.com/embed/{video_id}'
    elif 'youtube.com/watch' in value:
        match = re.search(r'v=([^&]+)', value)
        if match:
            video_id = match.group(1)
            return f'https://www.youtube.com/embed/{video_id}'
    elif 'youtube.com/live' in value:
        match = re.search(r'live/([^?&]+)', value)
        if match:
            video_id = match.group(1)
            return f'https://www.youtube.com/embed/{video_id}'
    return value

@register.filter(name='facebook_embed_url')
def facebook_embed_url(value):
    # Transformer les URL abrégées de Facebook Watch en URL complètes
    if 'fb.watch' in value:
        value = value.replace('https://fb.watch/', 'https://www.facebook.com/watch/?v=')
    
    if 'facebook.com' in value or 'fb.watch' in value:
        return f'https://www.facebook.com/plugins/video.php?href={value}&show_text=0&width=560'
    
    return value

@register.filter
def startswith(value, arg):
    return value.startswith(arg)
