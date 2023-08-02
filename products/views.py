from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def index(request):
    popular_products = Product.objects.order_by('-popularity')

    new_products = Product.objects.order_by('-pub_date')

    context = {
        'popular_products': popular_products,
        'new_products': new_products,
    }
    return render(request, 'products/product_screen.html', context)

def post_product(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        popularity = request.POST['popularity']

        if not popularity or not popularity.isdigit():
            popularity = 0
        else:
            popularity = int(popularity)

        image = request.FILES.get('image')

        new_product = Product(title=title, content=content, popularity=popularity, image=image)
        new_product.save()

        return redirect('products')

    return render(request, 'products/product_post.html')

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {'product': product}
    return render(request, 'products/product_delete.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    product.popularity += 1
    product.save()

    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

