from django import template
from oscar.core.loading import get_model

register = template.Library()
Category = get_model('catalogue', 'category')


@register.assignment_tag(name="root_categories")
def get_annotated_list(depth=None, parent=None):
    return Category.get_root_nodes()
