from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        if request.user.is_authenticated:
            text = request.POST['text']
            Comment.objects.create(
                product=product,
                author=request.user,
                text=text
            )
            return redirect('product_detail', pk=pk)

    return render(request, 'product_detail.html', {
        'product': product,
        'comments': comments
    })