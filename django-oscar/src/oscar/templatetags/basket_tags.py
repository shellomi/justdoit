from django import template

from oscar.core.loading import get_class, get_model

AddToBasketForm = get_class('basket.forms', 'AddToBasketForm')
SimpleAddToBasketForm = get_class('basket.forms', 'SimpleAddToBasketForm')
Product = get_model('catalogue', 'product')

register = template.Library()

QNT_SINGLE, QNT_MULTIPLE = 'single', 'multiple'


@register.assignment_tag()
def basket_form(request, product, quantity_type='single'):
    if not isinstance(product, Product):
        return ''

    initial = {}
    if not product.is_parent:
        initial['product_id'] = product.id

    form_class = AddToBasketForm
    if quantity_type == QNT_SINGLE:
        form_class = SimpleAddToBasketForm

    form = form_class(request.basket, product=product, initial=initial)

    return form


@register.simple_tag()
def is_product_in_cart(request, product):
    if not isinstance(product, Product):
        return False
    try:
        # if product.pk != 1:
        #     return False
        product_qty = request.basket.line_quantity(product, request.basket.strategy.fetch_for_product(product).stockrecord)
        return product_qty > 0
    except Exception as e:
        return False
