from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from reviews.models import Review
from django.contrib.auth.models import User
from reviews.forms import ReviewForm


def home_page(request):
    return render(request, 'catalog/home.html')

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = User.objects.first()
            new_review.save()

            return redirect('catalog:product_detail', product_id=product.id)

    else:
        form = ReviewForm()
        context = {
            'product': product,
            'reviews': reviews,
            'form': form
        }
        return render(request, 'catalog/product_detail.html', context)
