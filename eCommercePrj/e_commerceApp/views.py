from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from e_commerceApp.models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

def allProdCatView(request, c_slug=None):
    c_page = None
    product_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page, available=True)
    else :
        product_list = Product.objects.all().filter(available=True)
    
    paginator_v = Paginator(product_list,6)
    try:
        page_v = int(request.GET.get('page','1'))
    except:
        page_v = 1
        
    try:
        products = paginator_v.page(page_v)
    except (EmptyPage, InvalidPage):
        products = paginator_v.page(paginator_v.num_pages)
        
    return render(request,"category.html",{'category':c_page, 'products':products})

def proDetailView(request, c_slug,p_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

