from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

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