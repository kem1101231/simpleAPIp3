from types import MethodDescriptorType, ModuleType
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ast

from datetime import datetime 

from .models import Movies, Inventory, Product, Purchase, PurchaseLine, Supplier, Sales, SalesLine


def movies(request):
    movies = Movies.objects.all()
    context = {
        'movies':list(movies.values()),
    }

    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No movies to display")

@csrf_exempt
def addMovie(request):

    if request.method == 'POST':
        print("POST bay")

        request_body = request.body
        request_dict = request_body.decode("UTF-8")
        result = ast.literal_eval(request_dict)
        title = result['title']
        year_of_release = result['year_of_release']

        movie = Movies(title=title, year_of_release=year_of_release)
        movie.save()

    return HttpResponse("Done adding")

def getMovieDetails(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    movie_detail = {
        'title':movie.title,
        'year_of_realease':movie.year_of_release,
    }

    context = {
        'movie':movie_detail,
    }

    return JsonResponse(context)

def funtest(request):
    print(request.GET.get('data1'))
    print(request.GET)
    return HttpResponse("FFFFFF")


# ==================================================================
# Simple POS Functions

#Product
def getAllProducts(request):
    products = Product.objects.all()
    context = {
        'products':list(products.values()),
    }
    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No movies to display")

def getProductDetails(request, reference_id):
    product = Product.objects.get(id=reference_id)
    product_detail = {
        'name':product.name, 
        'uom':product.uom, 
        'barcode':product.barcode,
    }

    context = {
        'product':product_detail,
    }
    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No product to display")

@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        
        request_body = request.body
        request_dict = request_body.decode("UTF-8")
        result = ast.literal_eval(request_dict)
        
        name = result['name']
        uom = result['uom']
        barcode = result['barcode']

        product = Product(product=name, uom=uom, barcode=barcode)
        product.save()

    return HttpResponse("Done adding")

#Supplier
def getAllSuppliers(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers':list(suppliers.values()),
    }
    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No suppliers to display")

def getSupplierDetails(request, reference_id):
    supplier = Supplier.objects.get(id=reference_id)
    supplier_detail = {
        'name':supplier.name, 
        'uom':supplier.uom, 
        'barcode':supplier.barcode,
    }

    context = {
        'supplier':supplier_detail,
    }
    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No supplier to display")

@csrf_exempt
def addSupplier(request):
    if request.method == 'POST':
        
        request_body = request.body
        request_dict = request_body.decode("UTF-8")
        result = ast.literal_eval(request_dict)
        
        name = result['name']
        address = result['address']
        business_type = result['business_type']
        code = result['code']

        supplier = Supplier(name=name, address=address, business_type=business_type, code=code)
        supplier.save()

    return HttpResponse("Done adding")
#Purchases
def getAllPurchase(request):
    purchases = Purchase.objects.all()
    # purchase_list = list(purchases.values())

    # context_list = []

    # for line in purchase_list:
    #     purchase_lines = PurchaseLine.objects.get(purchase_parent=line.code)
    #     line_value = {
    #                     'code':line.code,
    #                     'date':line.date,
    #                     'supplier':line.supplier,
    #                     'total_cost':line.total_cost,
    #                     'lines':list(purchase_lines.values()),
    #     }
    #     context_list.append(line_value)

    context = {
        'purchase':list(purchases.values()),
    }
    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No suppliers to display")

def getPurchaseDetails(request, reference_id):
    purchase = Purchase.objects.get(id=reference_id)
    purchase_lines = PurchaseLine.objects.get(purchase_parent=purchase.code)
    purchase_detail = {
        'code':purchase.code, 
        'date':purchase.date, 
        'supplier':purchase.supplier,
        'total_cost':purchase.total_cost,
        'line':list(purchase_lines.values()),
    }

    context = {
        'purchase':purchase_detail,
    }
    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No supplier to display")

@csrf_exempt
def addPurchase(request):
    if request.method == 'POST':
        
        request_body = request.body
        request_dict = request_body.decode("UTF-8")
        result = ast.literal_eval(request_dict)
        
        code = result['code']
        date = datetime.today()
        supplier = result['supplier']
        total_cost = result['total_cost']
        line = result['line']

        for item in line:
            purchase_parent = item['parent']
            product_code = item['product']
            cost_per_unit = item['cost']
            quantity = item['qty']

            purchase_line = PurchaseLine(purchase_parent=purchase_parent, product_code=product_code, cost_per_unit=cost_per_unit, quantity=quantity)
            purchase_line.save()


        purchase = Purchase(code=code, date=date, supplier=supplier, total_cost=total_cost)
        purchase.save()

    return HttpResponse("Done adding")

# #Inventory
# def getAll(request):
#     return HttpResponse()
# def getDetails(request):
#     return HttpResponse()
# @csrf_exempt
# def add(request):
#     return HttpResponse()

# #Sales
# def getAll(request):
#     return HttpResponse()
# def getDetails(request):
#     return HttpResponse()
# @csrf_exempt
# def add(request):
#     return HttpResponse()
