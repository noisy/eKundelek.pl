from mezzanine.blog.models import BlogPost 
from mezzanine import template 

register = template.Library() 

@register.as_tag 
def random_selections(number = 5):
    return list(BlogPost.objects.published().order_by('?')[:number])
