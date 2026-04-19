from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .cart import Cart

def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)  # 4 товара на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'products': products , 'page_obj': page_obj
    })

def product_detail(request, pk):
   product = get_object_or_404(Product, pk=pk)
   comments = Comment.objects.filter(product=product)
   if request.method == 'POST':
       if request.user.is_authenticated:
           text = request.POST['text']
           Comment.objects.create(product=product, author=request.user, text=text)
           return redirect('product_detail', pk=pk)
   return render(request, 'product_detail.html', {'product': product, 'comments': comments})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_authenticated:
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)  # убрать лайк
        else:
            comment.likes.add(request.user)     # поставить лайк
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('product_list')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def product_list(request):
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 4)  # 4 товара на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'page_obj': page_obj
    })