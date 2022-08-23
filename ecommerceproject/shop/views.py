from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Catagory,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage



# Create your views here.
# def index(request):
#     return HttpResponse('hello world')


def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Catagory,slug=c_slug)
        products_list=Products.objects.all().filter(catagory=c_page,available=True)
    else:
        products_list=Products.objects.all().filter(available=True)
    paginator = Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except  (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'catagory.html',{'catagory':c_page,'products':products})


def proDetail(request,c_slug,product_slug):
    try:
        product = Products.objects.get(catagory__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
