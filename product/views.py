from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Product, Choice


def indexview(request):
    latest_product_list = Product.objects.all().order_by('-pub_date')[:6]
    return render(request, 'index.html', {'latest_product_list':latest_product_list})

def detailview(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'detail.html', {'product': product})


def votesview(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        selected_choice = product.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # redisplay the product voting form
        return render(request, 'detail.html', {
            'product':product,
            'error_message':"You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('product:result', args=str((product.id))))


def resultview(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'result.html', {'product':product})