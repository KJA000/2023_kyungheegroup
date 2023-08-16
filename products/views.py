from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Comment
from .forms import CommentForm
from django.core.exceptions import PermissionDenied

def index(request):
    popular_products = Product.objects.order_by('-popularity')

    new_products = Product.objects.order_by('-pub_date')

    context = {
        'popular_products': popular_products,
        'new_products': new_products,
        'active_page' : 'product',
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

    context = {'product': product, 'active_page' : 'product'}
    return render(request, 'products/product_detail.html', context)

@login_required(login_url='/users/')
def comment_create(request, product_id):
        content_list = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
           form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('product-detail', product_id=content_list.id)
        else:
            form = CommentForm()
            context = {'content_list': content_list, 'form': form, 'active_page' : 'product'}
        
        return render(request, 'products/product_detail.html', context)


@login_required(login_url='/users/')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('product-detail', product_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
    
    context = {'comment': comment, 'form': form, 'active_page' : 'product'}
    return render(request, 'products/comment_form.html', context)


@login_required(login_url='/users/')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    
    else:
        comment.delete()
    return redirect('product-detail', product_id=comment.content_list.id)
