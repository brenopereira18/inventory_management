from django.db.models import Sum, F
from django.utils import timezone
from django.utils.formats import number_format
from brands.models import Brand
from products.models import Product
from outflows.models import Outflow
from categories.models import Category


def get_product_metrics():
    products = Product.objects.all()
    total_quantity = sum(product.quantity for product in products)
    total_cost_price = sum(
        product.cost_price * product.quantity for product in products
    )
    total_selling_price = sum(
        product.selling_price * product.quantity for product in products
    )
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_quantity=total_quantity,
        total_cost_price=number_format(
            total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(
            total_selling_price, decimal_pos=2, force_grouping=True),
        total_profit=number_format(
            total_profit, decimal_pos=2, force_grouping=True),
    )


def get_sales_metrics():
    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(
        total_products_sold=Sum('quantity')
    )['total_products_sold'] or 0
    total_sales_value = sum(
        outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all()
    )
    total_sales_cost = sum(
        outflow.quantity * outflow.product.cost_price for outflow in Outflow.objects.all()
    )
    total_sales_profit = total_sales_value - total_sales_cost

    return dict(
        total_sales=total_sales,
        total_products_sold=total_products_sold,
        total_sales_value=number_format(
            total_sales_value, decimal_pos=2, force_grouping=True),
        total_sales_profit=number_format(
            total_sales_profit, decimal_pos=2, force_grouping=True),
    )


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(
        dates=dates,
        values=values,
    )


def get_quantity_products_sold_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quanties = list()

    for date in dates:
        quantity_products_sold = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            product_quantity=Sum('quantity')
        )['product_quantity'] or 0
        quanties.append(quantity_products_sold)

    return dict(
        dates=dates,
        values=quanties,
    )


def get_graphic_product_category_metric():
    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def get_graphic_product_brand_metric():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}

